import os
import csv
from datetime import datetime

def save_diary(image, stress=None, mood=None, sleep=None, note=""):
    os.makedirs("diary", exist_ok=True)
    os.makedirs("diary/history", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"diary/history/{timestamp}.png"
    image.save(filename)

    # Save metadata
    history_file = "diary/history.csv"
    file_exists = os.path.isfile(history_file)
    with open(history_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp","file","stress","mood","sleep","note"])
        writer.writerow([timestamp, filename, stress, mood, sleep, note])

    return filename

def load_history():
    history_file = "diary/history.csv"
    if not os.path.exists(history_file):
        import pandas as pd
        return pd.DataFrame(columns=["timestamp","file","stress","mood","sleep","note"])
    import pandas as pd
    df = pd.read_csv(history_file)
    return df.sort_values(by="timestamp", ascending=False)

