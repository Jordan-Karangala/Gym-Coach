from local_feedback import LocalFeedback
import json
import requests
import os
from dotenv import load_dotenv


class FeedbackEngine:

    def __init__(self, config):
        load_dotenv()  # Load .env
        self.config = config
        self.use_llm = config.get("feedback", {}).get("use_llm", False)
        self.llm_provider = config.get("feedback", {}).get("provider", "openai")
        # Get API key from environment
        if self.llm_provider == "openai":
            self.api_key = os.getenv("OPENAI_API_KEY")
        elif self.llm_provider == "gemini":
            self.api_key = os.getenv("GEMINI_API_KEY")
        else:
            self.api_key = None
        self.local_feedback = LocalFeedback()


    def _get_llm_feedback(self, exercise_name, rep_result, targets):

        # Safety check
        if rep_result.get("rep_duration") is None:
            return None

        min_angle = rep_result.get("min_angle")
        max_angle = rep_result.get("max_angle")
        rep_duration = rep_result.get("rep_duration")
        speed = rep_result.get("rep_speed_state")
        rep_count = rep_result.get("rep_count")

        actual_range = None
        if min_angle is not None and max_angle is not None:
            actual_range = max_angle - min_angle

        if min_angle is not None:
            min_angle = float(min_angle)

        if max_angle is not None:
            max_angle = float(max_angle)

        if actual_range is not None:
            actual_range = float(actual_range)

        ideal_extended = None
        ideal_flexed = None
        ideal_range = None

        if targets:
            ideal_extended = targets.get("ideal_extended")
            ideal_flexed = targets.get("ideal_flexed")
            ideal_range = targets.get("ideal_range")

        print(type(min_angle), type(max_angle))
        print(type(rep_duration), type(rep_count))

        payload_context = {
            "exercise": exercise_name,
            "rep_number": rep_count,
            "min_angle": min_angle,
            "max_angle": max_angle,
            "actual_range": actual_range,
            "rep_duration": rep_duration,
            "speed": speed,
            "ideal_extended": ideal_extended,
            "ideal_flexed": ideal_flexed,
            "ideal_range": ideal_range
        }

        system_prompt = (
            "You are a professional fitness coach. "
            "Provide short, actionable feedback (max 2 sentences). "
            "Be specific about range of motion, extension, depth, and speed. "
            "Do not explain numbers. Just coach."
        )

        user_prompt = (
                "Workout rep analysis:\n\n"
                + json.dumps(payload_context, indent=2)
                + "\n\nGive coaching feedback."
        )

        # ===============================
        # OPENAI
        # ===============================
        if self.llm_provider == "openai":

            url = "https://api.openai.com/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.4
            }

            response = requests.post(url, headers=headers, json=data, timeout=10)
            response.raise_for_status()

            result = response.json()
            return result["choices"][0]["message"]["content"].strip()

        # ===============================
        # GEMINI
        # ===============================
        elif self.llm_provider == "gemini":

            url = (
                    "https://generativelanguage.googleapis.com/v1/models/"
                    "gemini-2.0-flash:generateContent?key=" + self.api_key
            )

            data = {
                "contents": [
                    {
                        "parts": [
                            {"text": system_prompt + "\n\n" + user_prompt}
                        ]
                    }
                ]
            }

            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()

            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"].strip()

        return None


    def get_feedback(self, exercise_name, rep_result, form_targets):

        if self.use_llm and self.api_key:
            try:
                feedback = self._get_llm_feedback(
                    exercise_name,
                    rep_result,
                    form_targets
                )

                if feedback:
                    return feedback

            except Exception as e:

                print("LLM failed:", e)

        # fallback
        return self.local_feedback.get_feedback(
            exercise_name,
            rep_result
        )