import streamlit as st
import os
from PIL import Image

from core.emotion_parser import EmotionParser
from core.profile_builder import EmotionalProfile

from rendering.renderer import Renderer
from data_io.input_handler import load_csv, list_sample_csvs
from data_io.diary import save_diary, load_history

import config


# Page Setup
st.set_page_config(
    page_title="HorizonMind",
    layout="wide"
)

st.title("🌅 HorizonMind - Emotional Landscape AI")
st.markdown(
    """
    **HorizonMind** converts wellbeing data into colorful, textured emotional landscapes.
    Explore your emotional patterns visually!
    """
)


# Data Source Selection
st.sidebar.header("Data Source")
source = st.sidebar.radio(
    "Select input method:",
    ("Manual Entry", "Upload CSV", "Use Sample CSV")
)

stress = mood = sleep = 5
note = ""


# Manual Entry
if source == "Manual Entry":
    st.sidebar.subheader("Daily Wellbeing Input")
    stress = st.sidebar.slider("Stress Level (0–10)", 0, 10, 5)
    mood = st.sidebar.slider("Mood (0–10)", 0, 10, 5)
    sleep = st.sidebar.slider("Sleep Duration (hrs)", 0, 12, 7)
    note = st.sidebar.text_area("Reflection / Journal Entry")


# CSV Upload
elif source == "Upload CSV":
    uploaded = st.sidebar.file_uploader("Upload wellbeing CSV", type=["csv"])
    if uploaded:
        data = load_csv(uploaded)
        stress = data["stress"]
        mood = data["mood"]
        sleep = data["sleep"]
        note = data["notes"]
        st.sidebar.success("CSV loaded successfully")


# Sample CSV
elif source == "Use Sample CSV":
    samples = list_sample_csvs()
    if samples:
        selected = st.sidebar.selectbox("Choose a sample dataset", samples)
        path = os.path.join("assets", "samples", selected)
        data = load_csv(path)
        stress = data["stress"]
        mood = data["mood"]
        sleep = data["sleep"]
        note = data["notes"]
        st.sidebar.success(f"Loaded sample: {selected}")
    else:
        st.sidebar.warning("No sample CSV files found.")


# Emotion & Profile Pipeline
parser = EmotionParser()
emotion = parser.parse(note)

profile_obj = EmotionalProfile(
    stress=stress/10,
    mood=mood/10,
    sleep=sleep/12,
    emotion=emotion
).build()

# Convert profile to dict for renderer
profile = {
    "stress": profile_obj["stress"],
    "mood": profile_obj["mood"],
    "sleep": profile_obj["sleep"],
    "emotion": profile_obj["emotion"]
}

# Rendering
renderer = Renderer()
image = renderer.render(profile, width=config.CANVAS_WIDTH, height=config.CANVAS_HEIGHT)
st.image(image, caption="Generated Emotional Landscape", width='stretch')


# Save to Visual Diary
if st.button("💾 Save to Visual Diary"):
    path = save_diary(
        image,
        stress=stress,
        mood=mood,
        sleep=sleep,
        note=note
    )
    st.success(f"Saved to {path}")


# Diary / History Sidebar
st.sidebar.markdown("---")
st.sidebar.header("Visual Diary History")

history_df = load_history()
if not history_df.empty:
    selected_row = st.sidebar.selectbox(
        "Select a past entry",
        history_df["timestamp"] + " | Stress: " + history_df["stress"].astype(str)
    )
    row = history_df[history_df["timestamp"] == selected_row.split(" | ")[0]].iloc[0]
    past_image = Image.open(row["file"])
    st.sidebar.image(
        past_image,
        caption=f"Stress:{row['stress']} Mood:{row['mood']}",
        width='stretch'
    )
else:
    st.sidebar.write("No history yet. Generate some images first!")


# Interpretation Guide

st.markdown("---")
st.markdown(
    """
    ### 🧠 Visual Interpretation Guide
    - **Jagged colorful areas** → stress or emotional turbulence
    - **Smooth flowing regions** → calm/mood positive
    - **Fog/mist overlays** → poor sleep/fatigue

    *Reflective visualisation only — not a diagnostic tool.*
    """
)
