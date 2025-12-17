from arcade.gui.widgets.text import UITextArea
from utils.user_utils import load_user_settings, is_light
from config import config

class BaseLargeText(UITextArea):
    def __init__(self, text="", width=config.WINDOW_WIDTH // 2, height=config.WINDOW_HEIGHT // 2, font_size=24, **kwargs):

        base_color = tuple(load_user_settings().get("game_color", [64,0,0,255]))
        light = is_light(base_color)
        if "text_color" not in kwargs:
            kwargs["text_color"] = (0,0,0,255) if light else (255,255,255,255)
            
        super().__init__(
            text=text,
            width=width,
            height=height,
            font_size=font_size,
            multiline=True,
            wrap_lines=True,
            scroll_speed=20,
            **kwargs
        )
