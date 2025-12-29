import arcade
import arcade.gui
import time
from base.BaseView import BaseView
from base.BaseButton import BaseButton
from base.BaseText import BaseText
from utils import assets_utils
from config import config

class GameSelectionView(BaseView):
    def __init__(self):
        super().__init__()
        self.title_text = BaseText(text="Flotarix",font_size=64)
        self.texts_to_show.append(self.title_text)

        self.author_text = BaseText(text="Alonso",font_size=8)
        self.texts_to_show.append(self.author_text)

        self.version_text = BaseText(text=config.VERSION,font_size=8)
        self.texts_to_show.append(self.version_text)

        self.back_button = BaseButton("Atras", width = config.WINDOW_WIDTH * 0.25, when_clicked=self.on_click_back)
        self.prepare_button(self.back_button)

    def update_layout(self):

        self.title_text.x = self.window.width * 0.5
        self.title_text.y = self.window.height * 0.9

        self.author_text.x = self.window.width * 0.5
        self.author_text.y = self.window.height * 0.825

        self.version_text.x = self.window.width * 0.5
        self.version_text.y = self.window.height * 0.80625

        self.back_button.center_x = self.window.width * 0.5
        self.back_button.center_y = self.window.height * 0.05

    def on_draw(self):
        super().on_draw()

    def on_resize(self, width, height):
        super().on_resize(width, height)

    def on_show_view(self):
        super().on_show_view()

    def on_click_back(self, event: arcade.gui.UIOnClickEvent):
        print("back clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.MenuView import MenuView
        self.uimanager.clear()
        view = MenuView()
        self.window.show_view(view)