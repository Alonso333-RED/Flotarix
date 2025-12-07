import arcade

from config import config

class BaseWindow(arcade.Window):
    def __init__(self):
        super().__init__(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, config.WINDOW_TITLE, resizable=True)
        arcade.set_background_color(arcade.color.BLACK)
