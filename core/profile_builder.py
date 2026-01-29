class EmotionalProfile:
    def __init__(self, stress, mood, sleep, emotion):
        self.stress = stress
        self.mood = mood
        self.sleep = sleep
        self.emotion = emotion

    def build(self) -> dict:
        # Compute fatigue
        fatigue = max(0, 6 - self.sleep) / 6

        # Composite stress intensity
        composite = (
            (self.stress * 0.4)
            - (self.mood * 0.3)
            + (fatigue * 0.2)
            - (self.emotion.get("polarity", 0) * 0.1)
        )

        # Return a dictionary compatible with app.py
        return {
            "stress": min(max(composite, 0), 1),         
            "mood": self.mood,                           
            "sleep": self.sleep,                          
            "emotion": self.emotion.get("polarity", 0)    
        }
