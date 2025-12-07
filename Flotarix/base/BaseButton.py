from arcade.gui import UIFlatButton
from utils.user_utils import load_user_settings, is_light, adjust

class BaseButton(UIFlatButton):
    def __init__(self, text="Button", width=200, height=50):
        base_color = tuple(load_user_settings().get("color_theme", [64,0,0,255]))
        light = is_light(base_color)

        fg = (0,0,0,255) if light else (255,255,255,255)
        border = fg

        style = {
            "normal": UIFlatButton.UIStyle(bg=base_color,
                                           border=border,
                                           border_width=2,
                                           font_color=fg),
            "hover": UIFlatButton.UIStyle(bg=adjust(base_color, -32) if light else adjust(base_color, +32),
                                          border=border,
                                          border_width=2,
                                          font_color=fg),
            "press": UIFlatButton.UIStyle(bg=adjust(base_color, -64) if light else adjust(base_color, +64),
                                          border=border,
                                          border_width=2,
                                          font_color=fg),
            "disabled": UIFlatButton.UIStyle(bg=base_color,
                                             border=border,
                                             border_width=2,
                                             font_color=fg)
        }
        super().__init__(text=text, width=width, height=height, style=style)
