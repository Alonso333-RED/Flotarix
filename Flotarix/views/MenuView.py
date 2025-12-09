import arcade
import arcade.gui

from base.BaseView import BaseView
from base.BaseButton import BaseButton
from base.BaseText import BaseText

class MenuView(BaseView):
    def __init__(self):
        super().__init__()
        
        self.title_text = BaseText(
            text="Flotarix",font_size=128,
            x =self.window.width // 2, y=self.window.height * 4 // 5
        )
        self.start_button = BaseButton("Start Game", when_clicked=self.on_click_default)
        self.start_button.center_x = self.window.width // 2
        self.start_button.center_y = self.window.height // 2
        self.uimanager.add(self.start_button)

    def on_draw(self):
        super().on_draw()
        self.uimanager.draw()
        self.title_text.draw()