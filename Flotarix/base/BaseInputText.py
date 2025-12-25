import arcade
import arcade.gui
from config import config
from utils.user_utils import load_user_settings, is_light, adjust

class BaseInputText(arcade.gui.UIInputText):
    def __init__(self,
                 text="",
                 x=config.WINDOW_WIDTH // 2,
                 y=config.WINDOW_HEIGHT // 2,
                 width=config.WINDOW_WIDTH * 0.25,
                 height=config.WINDOW_HEIGHT * 0.1,
                 font_size=28,
                 base_color=tuple(load_user_settings().get("game_color", [64, 0, 0, 255])),
                 **kwargs):

        light = is_light(base_color)
        fg = (0, 0, 0, 255) if light else (255, 255, 255, 255)
        border = fg

        style = {
            "normal": arcade.gui.UIInputText.UIStyle(
                bg=base_color,
                border=border,
                border_width=2
            ),
            "hover": arcade.gui.UIInputText.UIStyle(
                bg=adjust(base_color, -32) if light else adjust(base_color, +32),
                border=border,
                border_width=2
            ),
            "press": arcade.gui.UIInputText.UIStyle(
                bg=adjust(base_color, -64) if light else adjust(base_color, +64),
                border=border,
                border_width=2
            ),
            "disabled": arcade.gui.UIInputText.UIStyle(
                bg=base_color,
                border=border,
                border_width=2
            ),
            "invalid": arcade.gui.UIInputText.UIStyle(
                bg=base_color,
                border=border,
                border_width=2
            )
        }

        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            text=text,
            font_size=font_size,
            text_color=fg,
            caret_color=fg,
            style=style,
            **kwargs
        )
