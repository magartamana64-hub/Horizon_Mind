from textblob import TextBlob

class EmotionParser:

    def parse(self, text: str) -> dict:
        if not text or text.strip() == "":
            return {"polarity": 0.0, "subjectivity": 0.0}

        blob = TextBlob(text)
        return {
            "polarity": blob.sentiment.polarity,
            "subjectivity": blob.sentiment.subjectivity
        }
