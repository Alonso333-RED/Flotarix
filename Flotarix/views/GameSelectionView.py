import arcade
import arcade.gui
from base.BaseView import BaseView
from base.BaseButton import BaseButton
from base.BaseText import BaseText
from utils import assets_utils
from utils.user_utils import load_user_fleets
from config import config

class GameSelectionView(BaseView):
    def __init__(self):
        super().__init__()
        self.title_text = BaseText(text="Flotarix",font_size=96)
        self.texts_to_show.append(self.title_text)

        self.author_text = BaseText(text="Alonso",font_size=16)
        self.texts_to_show.append(self.author_text)

        self.version_text = BaseText(text=config.VERSION,font_size=16)
        self.texts_to_show.append(self.version_text)

        self.back_button = BaseButton("Atras", width = config.WINDOW_WIDTH * 0.25, when_clicked=self.on_click_back)
        self.prepare_button(self.back_button)

        self.two_players_classic_button = BaseButton("2 Jugadores; Clasico", width = config.WINDOW_WIDTH * 0.375, when_clicked=self.on_click_two_players_classic)
        self.prepare_button(self.two_players_classic_button)

        self.four_players_classic_button = BaseButton("4 Jugadores; Clasico", width = config.WINDOW_WIDTH * 0.375, when_clicked=self.on_click_four_players_classic)
        self.prepare_button(self.four_players_classic_button)

        self.two_players_fast_button = BaseButton("Proximamente", width = config.WINDOW_WIDTH * 0.375, when_clicked=self.on_click_default)
        self.prepare_button(self.two_players_fast_button)

        self.four_players_fast_button = BaseButton("Proximamente", width = config.WINDOW_WIDTH * 0.375, when_clicked=self.on_click_default)
        self.prepare_button(self.four_players_fast_button)

        self.fleets = load_user_fleets()

        self.player_sprites = arcade.SpriteList()
        self.player1_sprite = assets_utils.load_ship_sprite("flagship", self.fleets["player1"]["flagship"], scale=0.125, color_splash=(self.player1_color[0],self.player1_color[1],self.player1_color[2],0.75))
        self.player2_sprite = assets_utils.load_ship_sprite("flagship", self.fleets["player2"]["flagship"], scale=0.125, color_splash=(self.player2_color[0],self.player2_color[1],self.player2_color[2],0.75))
        self.player3_sprite = assets_utils.load_ship_sprite("flagship", self.fleets["player3"]["flagship"], scale=0.125, color_splash=(self.player3_color[0],self.player3_color[1],self.player3_color[2],0.75))
        self.player4_sprite = assets_utils.load_ship_sprite("flagship", self.fleets["player4"]["flagship"], scale=0.125, color_splash=(self.player4_color[0],self.player4_color[1],self.player4_color[2],0.75))
        self.player_sprites.append(self.player1_sprite)
        self.player_sprites.append(self.player2_sprite)
        self.player_sprites.append(self.player3_sprite)
        self.player_sprites.append(self.player4_sprite)

        self.player1_settings_button = BaseButton(text = self.settings.get("player1_name", ""), width = config.WINDOW_WIDTH * 0.15625, base_color=tuple(self.player1_color), when_clicked=self.on_click_default)
        self.prepare_button(self.player1_settings_button)

        self.player2_settings_button = BaseButton(text = self.settings.get("player2_name", ""), width = config.WINDOW_WIDTH * 0.15625, base_color=tuple(self.player2_color), when_clicked=self.on_click_default)
        self.prepare_button(self.player2_settings_button)

        self.player3_settings_button = BaseButton(text = self.settings.get("player3_name", ""), width = config.WINDOW_WIDTH * 0.15625, base_color=tuple(self.player3_color), when_clicked=self.on_click_default)
        self.prepare_button(self.player3_settings_button)

        self.player4_settings_button = BaseButton(text = self.settings.get("player4_name", ""), width = config.WINDOW_WIDTH * 0.15625, base_color=tuple(self.player4_color), when_clicked=self.on_click_default)
        self.prepare_button(self.player4_settings_button)

    def update_layout(self):

        self.title_text.x = self.window.width * 0.5
        self.title_text.y = self.window.height * 0.9

        self.author_text.x = self.window.width * 0.5
        self.author_text.y = self.window.height * 0.775

        self.version_text.x = self.window.width * 0.5
        self.version_text.y = self.window.height * 0.7375

        self.back_button.center_x = self.window.width * 0.5
        self.back_button.center_y = self.window.height * 0.05

        self.two_players_classic_button.center_x = self.window.width * 0.5 - 150
        self.two_players_classic_button.center_y = self.window.height * 0.65

        self.four_players_classic_button.center_x = self.window.width * 0.5 + 150
        self.four_players_classic_button.center_y = self.window.height * 0.65

        self.two_players_fast_button.center_x = self.window.width * 0.5 - 150
        self.two_players_fast_button.center_y = self.window.height * 0.55

        self.four_players_fast_button.center_x = self.window.width * 0.5 + 150
        self.four_players_fast_button.center_y = self.window.height * 0.55

        self.player1_sprite.center_x = self.window.width * 0.5 - 300
        self.player1_sprite.center_y = self.window.height * 0.375

        self.player2_sprite.center_x = self.window.width * 0.5 - 100
        self.player2_sprite.center_y = self.window.height * 0.375

        self.player3_sprite.center_x = self.window.width * 0.5 + 100
        self.player3_sprite.center_y = self.window.height * 0.375

        self.player4_sprite.center_x = self.window.width * 0.5 + 300
        self.player4_sprite.center_y = self.window.height * 0.375

        self.player1_settings_button.center_x = self.window.width * 0.5 - 300
        self.player1_settings_button.center_y = self.window.height * 0.2

        self.player2_settings_button.center_x = self.window.width * 0.5 - 100
        self.player2_settings_button.center_y = self.window.height * 0.2

        self.player3_settings_button.center_x = self.window.width * 0.5 + 100
        self.player3_settings_button.center_y = self.window.height * 0.2

        self.player4_settings_button.center_x = self.window.width * 0.5 + 300
        self.player4_settings_button.center_y = self.window.height * 0.2

    def on_draw(self):
        super().on_draw()
        self.player_sprites.draw()

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

    def on_click_two_players_classic(self, event: arcade.gui.UIOnClickEvent):
        print("two_players_classic clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.ClassicGameView import ClassicGameView
        self.uimanager.clear()
        view = ClassicGameView(2)
        self.window.show_view(view)

    def on_click_four_players_classic(self, event: arcade.gui.UIOnClickEvent):
        print("two_players_classic clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.ClassicGameView import ClassicGameView
        self.uimanager.clear()
        view = ClassicGameView(4)
        self.window.show_view(view)