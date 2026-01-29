# HorizonMind


**Student name:** Tamana Magar
**Student number:** 2316703
**Project title:** HorizonMind - AI Visualizer for Mental Health Stress Patterns  


---

## Setup Instructions

Follow the steps below to set up and run the HorizonMind project.

### Clone the repository
```
git clone https://github.com/yourusername/HorizonMind.git
cd HorizonMind
```
### Create and activate a Python virtual environment
```
python -m venv venv
```

#### Activate
```
venv\Scripts\activate
```
### Install required Python packages
```
pip install --upgrade pip
pip install -r requirements.txt
```
- The requirements.txt includes all necessary packages for Streamlit, NumPy, Pillow, OpenCV, and NLP dependencies.

### Prepare sample data
- The assets/samples/ folder contains sample CSV files for testing.
- CSV format example:
```
stress,mood,sleep,notes
7,3,6,"Felt anxious and tired today."
2,8,8,"Had a calm and productive day."
5,5,7,"Normal day, nothing unusual."
```
- You can also create your own CSV following this format.

### Run the Streamlit application
```
python -m streamlit run app.py
```

## Features
- Manual Input: Enter daily stress, mood, sleep, and reflections.
- CSV Input: Upload your weekly or daily CSV data.
- Sample CSVs: Preloaded example datasets to test.
- Generative Emotional Landscapes: Procedural AI-lite mesh visualizations combining stress, mood, sleep, and emotion.
- Dynamic Colormaps: Colors reflect emotional state (stress → red/orange, calm → blue/green).
-Fog Overlay: Visualizes fatigue or poor sleep.
- Visual Diary: Save daily images and review past history in the sidebar.
- Canvas Stroke: Frames each generated image for clarity.

## Project Structure
```
HorizonMind/
│
├─ app.py                   # Main Streamlit application
├─ config.py                # Canvas size and general configurations
├─ requirements.txt         # Python dependencies
├─ README.md                # This file
│
├─ core/
│   ├─ emotion_parser.py    # NLP-based emotion extraction
│   └─ profile_builder.py   # Build emotional profile from input
│
├─ rendering/
│   └─ renderer.py          # Generates mesh + color + fog + stroke
│
├─ data_io/
│   ├─ input_handler.py     # Load CSV, list sample CSVs
│   └─ diary.py             # Save images and history
│
├─ assets/
│   └─ samples/             # Sample CSV files
└─ venv/                    # Virtual environment (ignored in git)
```

## How to Use
- Select Data Source from the sidebar (Manual Entry / Upload CSV / Sample CSV).
- Adjust sliders for Stress, Mood, Sleep and add reflection notes if using manual input.
- Click Generate Emotional Landscape.
- Optionally, click Save to Visual Diary to save the image and review later in the sidebar.