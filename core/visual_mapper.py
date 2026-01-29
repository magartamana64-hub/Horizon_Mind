class VisualMapper:

    def map(self, profile: dict) -> dict:
        return {
            "terrain_roughness": 20 + profile["stress_intensity"] * 120,
            "color_temperature": profile["calmness"],
            "glitch_strength": profile["stress_intensity"],
            "mist_density": profile["fatigue"],
            "flow_smoothness": 1 - profile["stress_intensity"]
        }
