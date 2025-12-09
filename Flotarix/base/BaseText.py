import arcade
from utils.user_utils import load_user_settings, is_light
from config import config

class BaseText(arcade.Text):
    def __init__(self, text="", x=config.WINDOW_WIDTH // 2, y=config.WINDOW_HEIGHT // 2,
                 color=None, font_size=14, anchor_x="center", anchor_y="center", **kwargs):
        base_color = tuple(load_user_settings().get("color_theme", [64,0,0,255]))
        light = is_light(base_color)

        if color is None:
            color = (0,0,0,255) if light else (255,255,255,255)

        super().__init__(
            text=text,
            x=x,
            y=y,
            color=color,
            font_size=font_size,
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            **kwargs
        )
