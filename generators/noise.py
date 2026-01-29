import numpy as np
import cv2

def perlin_noise(width, height, scale):
    noise = np.random.rand(height, width)
    return cv2.GaussianBlur(noise, (0, 0), scale)
