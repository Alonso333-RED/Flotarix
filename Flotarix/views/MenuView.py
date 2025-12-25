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
        
        self.title_text = BaseText(text="Flotarix",font_size=128)
        self.texts_to_show.append(self.title_text)

        self.author_text = BaseText(text="Alonso",font_size=16)
        self.texts_to_show.append(self.author_text)

        self.version_text = BaseText(text=config.VERSION,font_size=16)
        self.texts_to_show.append(self.version_text)

        self.start_button = BaseButton("Empezar", width = config.WINDOW_WIDTH * 0.5, when_clicked=self.on_click_default)
        self.prepare_button(self.start_button)

        self.news_button = BaseButton("Novedades", width = config.WINDOW_WIDTH * 0.25, when_clicked=self.on_click_news)
        self.prepare_button(self.news_button)

        self.settings_button = BaseButton("Ajustes", width = config.WINDOW_WIDTH * 0.25, when_clicked=self.on_click_settings)
        self.prepare_button(self.settings_button)

        self.help_button = BaseButton("Como jugar", width = config.WINDOW_WIDTH * 0.25, when_clicked=self.on_click_help)
        self.prepare_button(self.help_button)

        self.credits_button = BaseButton("Creditos", width = config.WINDOW_WIDTH * 0.25, when_clicked=self.on_click_credits)
        self.prepare_button(self.credits_button)

        self.exit_button = BaseButton("Salir", width = config.WINDOW_WIDTH * 0.25, when_clicked=self.on_click_exit)
        self.prepare_button(self.exit_button)

    def on_draw(self):
        super().on_draw()
        self.title_text.x = self.window.width * 0.5
        self.title_text.y = self.window.height * 0.8

        self.author_text.x = self.window.width * 0.5
        self.author_text.y = self.window.height * 0.64

        self.version_text.x = self.window.width * 0.5
        self.version_text.y = self.window.height * 0.6

        self.start_button.center_x = self.window.width * 0.5
        self.start_button.center_y = self.window.height * 0.5

        self.news_button.center_x = self.window.width * 0.5 + 100
        self.news_button.center_y = self.window.height * 0.4

        self.settings_button.center_x = self.window.width * 0.5 - 100
        self.settings_button.center_y = self.window.height * 0.4

        self.help_button.center_x = self.window.width * 0.5 + 100
        self.help_button.center_y = self.window.height * 0.3

        self.credits_button.center_x = self.window.width * 0.5 - 100
        self.credits_button.center_y = self.window.height * 0.3

        self.exit_button.center_x = self.window.width * 0.5
        self.exit_button.center_y = self.window.height * 0.2

    def on_click_settings(self, event: arcade.gui.UIOnClickEvent):
        print("response to settings button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.SettingsView import SettingsView
        self.uimanager.clear()
        view = SettingsView()
        self.window.show_view(view)

    def on_click_news(self, event: arcade.gui.UIOnClickEvent):
        print("response to news button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.NewsView import NewsView
        self.uimanager.clear()
        view = NewsView()
        self.window.show_view(view)

    def on_click_help(self, event: arcade.gui.UIOnClickEvent):
        print("response to help button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.HelpView import HelpView
        self.uimanager.clear()
        view = HelpView()
        self.window.show_view(view)

    def on_click_credits(self, event: arcade.gui.UIOnClickEvent):
        print("response to credits button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.CreditsView import CreditsView
        self.uimanager.clear()
        view = CreditsView()
        self.window.show_view(view)

    def on_click_exit(self, event: arcade.gui.UIOnClickEvent):
        print("response to exit button clicked.")
        assets_utils.execute_sound("exit.mp3", self.ui_volume)
        self.uimanager.clear()
        time.sleep(1)
        arcade.exit()
        exit()