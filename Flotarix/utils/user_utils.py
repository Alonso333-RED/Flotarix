import json
from pathlib import Path
from utils.math_utils import clamp

BASE_DIR = Path(__file__).resolve().parent.parent
USER_SETTINGS_FILE = BASE_DIR / "user_data" / "settings.json"

DEFAULT_SETTINGS = {
    "ui_volume": 1.0,
    "effects_volume": 1.0,
    "game_color": [
        64,
        0,
        0
    ],
    "player1_name": "Jugador1",
    "player1_color": [
        255,
        0,
        0
    ],
    "player2_name": "Jugador2",
    "player2_color": [
        0,
        0,
        255
    ],
    "player3_name": "Jugador3",
    "player3_color": [
        0,
        255,
        0
    ],
    "player4_name": "Jugador4",
    "player4_color": [
        255,
        255,
        0
    ],
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

def save_user_settings(settings):
    USER_SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(USER_SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def save_game_color(red_requester, green_requester, blue_requester):
    settings = load_user_settings()

    current_color = settings.get("game_color", [64, 0, 0])

    try:
        red = int(red_requester.text.strip()) if red_requester.text.strip() != "" else current_color[0]
        green = int(green_requester.text.strip()) if green_requester.text.strip() != "" else current_color[1]
        blue = int(blue_requester.text.strip()) if blue_requester.text.strip() != "" else current_color[2]

        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            print("RGB out of range")
            return

    except ValueError:
        print("Invalid RGB")
        return

    settings["game_color"] = [red, green, blue]
    save_user_settings(settings)


def save_player(name_requester, name_key, red_requester, green_requester, blue_requester, color_key):
    settings = load_user_settings()
    changed = False

    name = name_requester.text.strip()
    if name:
        settings[name_key] = name[:10]
        changed = True

    current_color = settings.get(color_key, [64, 0, 0])

    try:
        red = int(red_requester.text.strip()) if red_requester.text.strip() != "" else current_color[0]
        green = int(green_requester.text.strip()) if green_requester.text.strip() != "" else current_color[1]
        blue = int(blue_requester.text.strip()) if blue_requester.text.strip() != "" else current_color[2]

        if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
            settings[color_key] = [red, green, blue]
            changed = True
        else:
            print("new RGB out of range")

    except ValueError:
        print("Invalid RGB")

    if changed:
        save_user_settings(settings)

def save_volume_to(ui_volume_requester, effects_volume_requester):
    new_ui_volume = ui_volume_requester.text.strip()
    new_effects_volume = effects_volume_requester.text.strip()

    settings = load_user_settings()
    current_ui_volume = settings.get("ui_volume", 1.0)
    current_effects_volume = settings.get("effects_volume", 1.0)

    try:
        new_ui_volume = float(new_ui_volume) / 100.0 if new_ui_volume != "" else current_ui_volume
    except ValueError:
        print("Invalid value for UI Volume")
        return

    try:
        new_effects_volume = float(new_effects_volume) / 100.0 if new_effects_volume != "" else current_effects_volume
    except ValueError:
        print("Invalid value for Effects Volume")
        return
    
    new_ui_volume = clamp(new_ui_volume, 0.0, 1.0)
    new_effects_volume = clamp(new_effects_volume, 0.0, 1.0)

    settings["ui_volume"] = new_ui_volume
    settings["effects_volume"] = new_effects_volume

    save_user_settings(settings)

def is_light(color):
    r, g, b = color
    brightness = (r*299 + g*587 + b*114) / 1000
    return brightness > 128

def adjust(color, delta):
    adjusted = tuple(max(0, min(255, c + delta)) for c in color)
    return (adjusted[0], adjusted[1], adjusted[2], adjusted[3] if len(adjusted) > 3 else 255)
