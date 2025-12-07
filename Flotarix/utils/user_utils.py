import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
USER_SETTINGS_FILE = BASE_DIR / "user_data" / "settings.json"

DEFAULT_SETTINGS = {
    "username": "Player",
    "color_theme": [64, 0, 0],
}

def load_user_settings():

    USER_SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not USER_SETTINGS_FILE.exists():
        with open(USER_SETTINGS_FILE, "w") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
        return DEFAULT_SETTINGS.copy()
    
    with open(USER_SETTINGS_FILE, "r") as f:
        data = json.load(f)

    settings = DEFAULT_SETTINGS.copy()
    settings.update(data)
    
    return settings

def is_light(color):
    r, g, b = color
    brightness = (r*299 + g*587 + b*114) / 1000
    return brightness > 128

def adjust(color, delta):
    adjusted = tuple(max(0, min(255, c + delta)) for c in color)
    return (adjusted[0], adjusted[1], adjusted[2], adjusted[3] if len(adjusted) > 3 else 255)
