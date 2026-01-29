import cv2
import random

def add_cracks(canvas, strength):
    h, w, _ = canvas.shape
    for _ in range(int(strength * 80)):
        x1, y1 = random.randint(0, w), random.randint(0, h)
        x2, y2 = x1 + random.randint(-120, 120), y1 + random.randint(-120, 120)
        cv2.line(canvas, (x1, y1), (x2, y2), (20, 20, 20), 1)
    return canvas


def add_mist(canvas, density):
    if density <= 0:
        return canvas
    blur = int(density * 15) * 2 + 1
    return cv2.GaussianBlur(canvas, (blur, blur), 0)
