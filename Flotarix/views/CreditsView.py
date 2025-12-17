import arcade
import arcade.gui
from base.BaseView import BaseView
from base.BaseText import BaseText
from base.BaseLargeText import BaseLargeText
from base.BaseButton import BaseButton
from utils import assets_utils
from config import config

class CreditsView(BaseView):
    def __init__(self):
        super().__init__()

        self.title_text = BaseText(text="Flotarix",font_size=128)
        self.texts_to_show.append(self.title_text)

        self.author_text = BaseText(text="Alonso",font_size=16)
        self.texts_to_show.append(self.author_text)

        self.version_text = BaseText(text=config.VERSION,font_size=16)
        self.texts_to_show.append(self.version_text)

        self.credits_text = "Diseñado y programado por Alonso.\nTodos los recursos usados fueron creados por mí o tomados de bibliotecas de assets libres.\n¡Gracias por jugar Flotarix!"

        self.credits_text_space = BaseLargeText(self.credits_text, 
                                        width=self.window.width * 3 // 4,
                                        height=self.window.height // 3,
                                        font_size=18)
        
        self.uimanager.add(self.credits_text_space)

        self.back_button = BaseButton("Atras", width = config.WINDOW_WIDTH//4, when_clicked=self.on_click_back)
        self.prepare_button(self.back_button)

    def on_draw(self):
        super().on_draw()
        self.title_text.x = self.window.width // 2
        self.title_text.y = self.window.height * 4 // 5

        self.author_text.x = self.window.width // 2
        self.author_text.y = self.window.height * 175 // 275

        self.version_text.x = self.window.width // 2
        self.version_text.y = self.window.height * 14 // 24

        self.credits_text_space.center_x = self.window.width // 2
        self.credits_text_space.center_y = self.window.height * 14 // 36

        self.back_button.center_x = self.window.width // 2
        self.back_button.center_y = self.window.height // 6

    def on_click_back(self, event: arcade.gui.UIOnClickEvent):
        print("response to back button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.MenuView import MenuView
        self.uimanager.clear()
        view = MenuView()
        self.window.show_view(view)