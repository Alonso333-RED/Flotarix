import arcade
import arcade.gui

import time

from base.BaseView import BaseView
from base.BaseButton import BaseButton
from base.BaseText import BaseText

from utils import assets_utils

from config import config

class MenuView(BaseView):
    def __init__(self):
        super().__init__()
        
        self.title_text = BaseText(
            text="Flotarix",font_size=128,
            x =self.window.width // 2, y=self.window.height * 4 // 5
        )
        self.texts_to_show.append(self.title_text)

        self.author_text = BaseText(
            text="Alonso",font_size=16,
            x =self.window.width // 2, y=self.window.height * 175 // 275
        )
        self.texts_to_show.append(self.author_text)

        self.version_text = BaseText(
            text=config.VERSION,font_size=16,
            x =self.window.width // 2, y=self.window.height * 14 // 24
        )
        self.texts_to_show.append(self.version_text)

        self.start_button = BaseButton("Start Game", width = config.WINDOW_WIDTH//2, when_clicked=self.on_click_default)
        self.start_button.center_x = self.window.width // 2
        self.start_button.center_y = self.window.height // 2
        self.prepare_button(self.start_button)

        self.news_button = BaseButton("News", width = config.WINDOW_WIDTH//4, when_clicked=self.on_click_news)
        self.news_button.center_x = self.window.width // 2 + 100
        self.news_button.center_y = self.window.height // 2.5
        self.prepare_button(self.news_button)

        self.settings_button = BaseButton("Settings", width = config.WINDOW_WIDTH//4, when_clicked=self.on_click_default)
        self.settings_button.center_x = self.window.width // 2 - 100
        self.settings_button.center_y = self.window.height // 2.5
        self.prepare_button(self.settings_button)

        self.help_button = BaseButton("Help", width = config.WINDOW_WIDTH//4, when_clicked=self.on_click_default)
        self.help_button.center_x = self.window.width // 2 + 100
        self.help_button.center_y = self.window.height // 3.25
        self.prepare_button(self.help_button)

        self.credits_button = BaseButton("Credits", width = config.WINDOW_WIDTH//4, when_clicked=self.on_click_default)
        self.credits_button.center_x = self.window.width // 2 - 100
        self.credits_button.center_y = self.window.height // 3.25
        self.prepare_button(self.credits_button)

        self.exit_button = BaseButton("Exit", width = config.WINDOW_WIDTH//4, when_clicked=self.on_click_exit)
        self.exit_button.center_x = self.window.width // 2
        self.exit_button.center_y = self.window.height // 4.75
        self.prepare_button(self.exit_button)

    def on_draw(self):
        super().on_draw()

    def on_click_news(self, event: arcade.gui.UIOnClickEvent):
        print("response to news button clicked.")
        assets_utils.execute_sound("click.mp3")
        from views.NewsView import NewsView
        self.uimanager.clear()
        view = NewsView()
        self.window.show_view(view)

    def on_click_exit(self, event: arcade.gui.UIOnClickEvent):
        print("response to exit button clicked.")
        assets_utils.execute_sound("exit.mp3")
        self.uimanager.clear()
        time.sleep(1)
        arcade.exit()
        exit()