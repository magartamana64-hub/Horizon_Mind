import numpy as np
from generators.noise import perlin_noise

def generate_terrain(width, height, roughness):
    base = perlin_noise(width, height, roughness)
    horizon = int(height * 0.55)

    terrain = np.zeros((height, width))
    for y in range(horizon, height):
        terrain[y] = base[y] * (y - horizon)

    return terrain
