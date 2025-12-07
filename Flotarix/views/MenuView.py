import arcade
import arcade.gui

from base.BaseView import BaseView
from base.BaseButton import BaseButton

class MenuView(BaseView):
    def __init__(self):
        super().__init__()

        self.start_button = BaseButton()
        self.start_button.center_x = self.window.width // 2
        self.start_button.center_y = self.window.height // 2 - 50
        self.uimanager.add(self.start_button)

    def on_draw(self):
        super().on_draw()
        self.uimanager.draw()