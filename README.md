🏋️ AI Gym Coach — Real-Time Exercise Form Analyzer


<p align="center">
  <img src="![squat sample](https://github.com/user-attachments/assets/e285588f-2374-478b-b873-8c787e9afacb)" width="100%">
</p>


![pushup sample](https://github.com/user-attachments/assets/5b3f0b95-9864-41ad-9dfc-f8c400412855)



A real-time computer vision system that detects exercise form, counts reps, evaluates movement quality, and provides AI-generated coaching feedback.

Built using pose estimation, configurable biomechanics logic, and LLM-powered feedback.

🚀 Features
🎥 Real-Time Pose Detection

YOLO-based pose estimation

Configurable for multiple exercises

Active side detection (left/right locking)

📐 Biomechanics Engine

Joint angle calculation (elbow, knee, hip, shoulder)

Config-driven angle definitions

Dynamic state machine (flexed → extended)

Rep start and rep completion detection

🔁 Rep Counting Logic

Angle range validation

Minimum range requirement

Speed classification (fast / good / slow)

Movement state tracking per frame

🧠 AI Coaching Feedback

LLM integration (OpenAI / Gemini)

Context-aware feedback per rep

Fallback to local feedback system

Rolling feedback support

📊 Workout Logging

CSV logging per session

Rep duration tracking

Min/max angle tracking

Speed performance recording

📈 Analytics-Ready Architecture

Session summary support

Progress tracking

Average rep speed

Total reps per session

🏗 Architecture Overview
Video Frame
    ↓
Pose Detection (YOLO)
    ↓
Keypoint Processing
    ↓
Angle Calculation (Config-driven)
    ↓
Side Locker
    ↓
Rep Counter (State Machine)
    ↓
Feedback Engine (LLM + Local fallback)
    ↓
Visualizer (Skeleton + Progress + Stats)
    ↓
Workout Logger
🧠 State Machine Logic

Each rep follows:

Extended → Flexed → Extended

Conditions for valid rep:

Minimum angle range achieved

Required flexed threshold reached

Required extended threshold reached

Speed classified within thresholds

⚙️ Config-Driven Design

Each exercise defines:

"angle_definition": {
    "left": ["jointA", "jointB", "jointC"],
    "right": ["jointA", "jointB", "jointC"]
},

"angle_thresholds": {
    "extended": 165,
    "flexed": 80,
    "min_range": 70
},

"speed_thresholds": {
    "fast": 0.8,
    "slow": 3.0
}

This allows:

Adding new exercises without modifying logic

Switching angle types dynamically

Customizing per-exercise biomechanics

🧪 Supported Exercises

Push-up

Bicep Curl

Tricep Extension

Shoulder Press

Lateral Raise

Front Raise

Bent-over Row

Pull-up

Squat

Lunge

Leg Extension

Leg Curl

Calf Raise

Deadlift

Sit-up

Crunch

🧠 LLM Integration

Optional AI coaching per rep using:

OpenAI API

Google Gemini API

If API fails → automatic fallback to local rule-based feedback.

Environment variable setup:

OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
📦 Installation
pip install -r requirements.txt

Run:

python main.py
🏁 Future Improvements

MediaPipe mobile-ready mode

Real-time dashboard UI

Multi-person tracking

Workout history analytics

Voice coaching

👨‍💻 Author

Machine Learning Engineer specializing in real-time computer vision systems and applied AI for biomechanics.
