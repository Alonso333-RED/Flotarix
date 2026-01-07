from utils import path_utils
from PIL import Image
import arcade
import json
from core.Spaceship import Spaceship, SpaceshipRecipe

def execute_sound(sound: str, volume: float = 1.0, splash: tuple = (0,0,0,0)):
    sound_path = path_utils.get_relative_path(f"assets/sounds/{sound}")
    sound_effect = arcade.load_sound(sound_path)
    arcade.play_sound(sound_effect, volume=volume)

_texture_cache = {}

def load_ship_recipe (ship: str) -> SpaceshipRecipe:
    recipe_path = path_utils.get_relative_path(
        f"assets/ships/{ship}/{ship}.json"
    )
    with open(recipe_path, "r") as file:
        data = json.load(file)
    recipe = SpaceshipRecipe(data)
    return recipe

def load_ship_sprite(
    ship: str,
    scale: float = 1.0,
    color_splash: tuple[int, int, int, float] | None = None,
) -> arcade.Sprite:

    sprite_path = path_utils.get_relative_path(
        f"assets/ships/{ship}/{ship}.png"
    )

    if color_splash is None:
        return arcade.Sprite(sprite_path, scale)

    key = (ship, color_splash)
    if key in _texture_cache:
        return arcade.Sprite(_texture_cache[key], scale)

    r, g, b, strength = color_splash

    img = Image.open(sprite_path)
    img = apply_color_splash(img, r, g, b, strength)

    texture = arcade.Texture(
        name=f"{ship}_{r}_{g}_{b}_{strength}",
        image=img
    )

    _texture_cache[key] = texture
    return arcade.Sprite(texture, scale)

def apply_color_splash(
    img: Image.Image,
    r: int,
    g: int,
    b: int,
    strength: float
) -> Image.Image:

    strength = max(0.0, min(1.0, strength))
    img = img.convert("RGBA")

    src_r, src_g, src_b, src_a = img.split()

    new_r = src_r.point(lambda i: int(i * (1 - strength) + r * strength))
    new_g = src_g.point(lambda i: int(i * (1 - strength) + g * strength))
    new_b = src_b.point(lambda i: int(i * (1 - strength) + b * strength))

    return Image.merge("RGBA", (new_r, new_g, new_b, src_a))