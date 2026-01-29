import numpy as np
from matplotlib import cm
from PIL import Image, ImageDraw, ImageEnhance

def generate_emotional_mesh(width, height, profile):
    """
    Generates a colorful mesh combining stress, mood, sleep, and emotion.
    """
    x = np.linspace(0, 4*np.pi, width)
    y = np.linspace(0, 4*np.pi, height)
    X, Y = np.meshgrid(x, y)

    # Waves representing each dimension
    stress_wave = np.sin(X * (1 + profile["stress"]*3))
    mood_wave   = np.cos(Y * (1 + profile["mood"]*3))
    sleep_wave  = np.sin((X+Y) * (0.2 + 0.5*profile["sleep"]))
    emotion_wave = np.sin(X*Y*profile["emotion"]*2)

    combined = stress_wave*0.4 + mood_wave*0.3 + sleep_wave*0.2 + emotion_wave*0.1

    # Normalize 0-1
    mesh = (combined - combined.min()) / (combined.max() - combined.min() + 1e-5)
    return mesh

def select_dynamic_colormap(stress, mood):
    """
    Select a colormap based on stress and mood:
    - High stress → warm colors
    - Low stress + high mood → cool colors
    """
    if stress > 0.6:
        return 'inferno'    # red/orange/purple
    elif stress > 0.3:
        return 'plasma'     # mixed warm
    elif mood > 0.5:
        return 'viridis'    # blue/green
    else:
        return 'cividis'    # neutral/pale
        

def mesh_to_color_image(mesh, colormap):
    cmap = cm.get_cmap(colormap)
    colored = cmap(mesh)[:, :, :3]  # ignore alpha
    img = (colored*255).astype(np.uint8)
    return img

def add_fog_overlay(img, fatigue_level=0.0):
    """
    Adds subtle fog overlay based on fatigue (0-1)
    """
    if fatigue_level <= 0:
        return img

    img_pil = Image.fromarray(img).convert("RGBA")
    fog = Image.new("RGBA", img_pil.size, (255,255,255,int(255*fatigue_level*0.5)))
    img_pil = Image.alpha_composite(img_pil, fog)
    return img_pil.convert("RGB")

def add_stroke(img, width=8, color=(0,0,0)):
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.rectangle([0,0,img_pil.width-1,img_pil.height-1], outline=color, width=width)
    return img_pil

class Renderer:
    def render(self, profile, width=225, height=135):
        # Generate emotional mesh
        mesh = generate_emotional_mesh(width, height, profile)

        # Choose colormap based on stress/mood
        colormap = select_dynamic_colormap(profile["stress"], profile["mood"])

        # Convert mesh to color image
        colored = mesh_to_color_image(mesh, colormap)

        # Add fog for fatigue (sleep factor)
        fatigue = max(0, 1-profile["sleep"])  # inverse sleep
        colored_with_fog = add_fog_overlay(colored, fatigue_level=fatigue)

        # Add canvas stroke
        final_img = add_stroke(np.array(colored_with_fog), width=8)
        return final_img
