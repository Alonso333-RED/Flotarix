import arcade
from utils import user_utils


class BaseView(arcade.View):
    def __init__(self):
        super().__init__()
        self.settings = user_utils.load_user_settings()
        self.background_color = self.settings["color_theme"]
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

    def on_draw(self):
        self.clear()