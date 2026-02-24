<h1 align="center">🏋️ AI Gym Coach — Real-Time Exercise Form Analyzer</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/e285588f-2374-478b-b873-8c787e9afacb" width="45%">
  &nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/5b3f0b95-9864-41ad-9dfc-f8c400412855" width="45%">
</p>

<p align="center">
  <em>Real-time Squat & Push-up Form Analysis</em>
</p>
---

<hr>

<h2 align="center">🚀 Overview</h2>

<p align="center">
A real-time computer vision system that detects exercise form,
counts repetitions, evaluates movement quality,
and generates AI-powered coaching feedback.
</p>

<p align="center">
Built using pose estimation, configurable biomechanics logic,
and LLM-powered feedback.
</p>

<hr>

<h2 align="center">🚀 Features</h2>

<h3>🎥 Real-Time Pose Detection</h3>
<ul>
  <li>YOLO-based pose estimation</li>
  <li>Configurable for multiple exercises</li>
  <li>Active side detection (left/right locking)</li>
</ul>

<h3>📐 Biomechanics Engine</h3>
<ul>
  <li>Joint angle calculation (elbow, knee, hip, shoulder)</li>
  <li>Config-driven angle definitions</li>
  <li>Dynamic state machine (flexed → extended)</li>
  <li>Rep start and rep completion detection</li>
</ul>

<h3>🔁 Rep Counting Logic</h3>
<ul>
  <li>Angle range validation</li>
  <li>Minimum range requirement</li>
  <li>Speed classification (fast / good / slow)</li>
  <li>Movement state tracking per frame</li>
</ul>

<h3>🧠 AI Coaching Feedback</h3>
<ul>
  <li>LLM integration (OpenAI / Gemini)</li>
  <li>Context-aware feedback per rep</li>
  <li>Fallback to local feedback system</li>
  <li>Rolling feedback support</li>
</ul>

<h3>📊 Workout Logging</h3>
<ul>
  <li>CSV logging per session</li>
  <li>Rep duration tracking</li>
  <li>Min/max angle tracking</li>
  <li>Speed performance recording</li>
</ul>

<h3>📈 Analytics-Ready Architecture</h3>
<ul>
  <li>Session summary support</li>
  <li>Progress tracking</li>
  <li>Average rep speed</li>
  <li>Total reps per session</li>
</ul>

<hr>

<h2 align="center">🏗 Architecture Overview</h2>

<pre>
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
</pre>

<hr>

<h2 align="center">🧠 State Machine Logic</h2>

<p align="center"><b>Extended → Flexed → Extended</b></p>

<p><b>Conditions for valid rep:</b></p>
<ul>
  <li>Minimum angle range achieved</li>
  <li>Required flexed threshold reached</li>
  <li>Required extended threshold reached</li>
  <li>Speed classified within thresholds</li>
</ul>

<hr>

<h2 align="center">⚙️ Config-Driven Design</h2>

<p>Each exercise defines:</p>

<pre>
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
</pre>

<p><b>This allows:</b></p>
<ul>
  <li>Adding new exercises without modifying logic</li>
  <li>Switching angle types dynamically</li>
  <li>Customizing per-exercise biomechanics</li>
</ul>

<hr>

<h2 align="center">🧪 Supported Exercises</h2>

<div align="center">

Push-up • Bicep Curl • Tricep Extension • Shoulder Press • Lateral Raise •  
Front Raise • Bent-over Row • Pull-up • Squat • Lunge •  
Leg Extension • Leg Curl • Calf Raise • Deadlift • Sit-up • Crunch  

</div>

<hr>

<h2 align="center">🧠 LLM Integration</h2>

<p align="center">
Optional AI coaching per rep using OpenAI API or Google Gemini API.
If API fails → automatic fallback to local rule-based feedback.
</p>

<h4>Environment Variables</h4>

<pre>
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
</pre>

<hr>

<h2 align="center">📦 Installation</h2>

<pre>
pip install -r requirements.txt
python main.py
</pre>

<hr>

<h2 align="center">🏁 Future Improvements</h2>

<ul>
  <li>MediaPipe mobile-ready mode</li>
  <li>Real-time dashboard UI</li>
  <li>Multi-person tracking</li>
  <li>Workout history analytics</li>
  <li>Voice coaching</li>
</ul>

<hr>

<h2 align="center">👨‍💻 Author</h2>

<p align="center">
Machine Learning Engineer specializing in real-time computer vision systems
and applied AI for biomechanics.
</p>

<hr>
