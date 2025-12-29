import arcade
import arcade.gui
from base.BaseView import BaseView
from base.BaseButton import BaseButton
from base.BaseText import BaseText
from base.BaseInputText import BaseInputText
from utils import assets_utils
from utils import user_utils
from config import config

class SettingsView(BaseView):
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


        self.game_color_text = BaseText(text="Color del juego",font_size=28)
        self.texts_to_show.append(self.game_color_text)

        self.game_color_red_input = BaseInputText(text = str(self.game_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.game_color_green_input = BaseInputText(text = str(self.game_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.game_color_blue_input = BaseInputText(text = str(self.game_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.game_color_red_input)
        self.uimanager.add(self.game_color_green_input)
        self.uimanager.add(self.game_color_blue_input)

        self.save_game_color_button = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_game_color)
        self.prepare_button(self.save_game_color_button)


        self.player1_text_indicator = BaseText(text="1: ",font_size=28)
        self.texts_to_show.append(self.player1_text_indicator)

        self.player1_name_input = BaseInputText(text = self.settings.get("player1_name", ""),width=config.WINDOW_WIDTH * 0.275, base_color=tuple(self.player1_color))
        self.player1_color_red_input = BaseInputText(text = str(self.player1_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.player1_color_green_input = BaseInputText(text = str(self.player1_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.player1_color_blue_input = BaseInputText(text = str(self.player1_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.player1_name_input)
        self.uimanager.add(self.player1_color_red_input)
        self.uimanager.add(self.player1_color_green_input)
        self.uimanager.add(self.player1_color_blue_input)

        self.save_player1_button = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_player1)
        self.prepare_button(self.save_player1_button)


        self.player2_text_indicator = BaseText(text="2: ",font_size=28)
        self.texts_to_show.append(self.player2_text_indicator)

        self.player2_name_input = BaseInputText(text = self.settings.get("player2_name", ""),width=config.WINDOW_WIDTH * 0.275, base_color=tuple(self.player2_color))
        self.player2_color_red_input = BaseInputText(text = str(self.player2_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.player2_color_green_input = BaseInputText(text = str(self.player2_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.player2_color_blue_input = BaseInputText(text = str(self.player2_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.player2_name_input)
        self.uimanager.add(self.player2_color_red_input)
        self.uimanager.add(self.player2_color_green_input)
        self.uimanager.add(self.player2_color_blue_input)

        self.save_player2_button = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_player2)
        self.prepare_button(self.save_player2_button)


        self.player3_text_indicator = BaseText(text="3: ",font_size=28)
        self.texts_to_show.append(self.player3_text_indicator)

        self.player3_name_input = BaseInputText(text = self.settings.get("player3_name", ""),width=config.WINDOW_WIDTH * 0.275, base_color=tuple(self.player3_color))
        self.player3_color_red_input = BaseInputText(text = str(self.player3_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.player3_color_green_input = BaseInputText(text = str(self.player3_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.player3_color_blue_input = BaseInputText(text = str(self.player3_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.player3_name_input)
        self.uimanager.add(self.player3_color_red_input)
        self.uimanager.add(self.player3_color_green_input)
        self.uimanager.add(self.player3_color_blue_input)

        self.save_player3_button = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_player3)
        self.prepare_button(self.save_player3_button)


        self.player4_text_indicator = BaseText(text="4: ",font_size=28)
        self.texts_to_show.append(self.player4_text_indicator)

        self.player4_name_input = BaseInputText(text = self.settings.get("player4_name", ""),width=config.WINDOW_WIDTH * 0.275, base_color=tuple(self.player4_color))
        self.player4_color_red_input = BaseInputText(text = str(self.player4_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.player4_color_green_input = BaseInputText(text = str(self.player4_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.player4_color_blue_input = BaseInputText(text = str(self.player4_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.player4_name_input)
        self.uimanager.add(self.player4_color_red_input)
        self.uimanager.add(self.player4_color_green_input)
        self.uimanager.add(self.player4_color_blue_input)

        self.save_player4_button = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_player4)
        self.prepare_button(self.save_player4_button)


        self.volume_text_indicator = BaseText(text="Volumen (0-100): ",font_size=28)
        self.texts_to_show.append(self.volume_text_indicator)

        self.ui_volume_text_indicator = BaseText(text="Interfaz: ",font_size=21)
        self.texts_to_show.append(self.ui_volume_text_indicator)
        self.ui_volume_input = BaseInputText(text = str(int(self.ui_volume*100)),width=config.WINDOW_WIDTH * 0.065625, height=config.WINDOW_HEIGHT * 0.075 ,font_size = 21, base_color= self.game_color)
        self.uimanager.add(self.ui_volume_input)


        self.effects_volume_text_indicator = BaseText(text="Efectos: ",font_size=21)
        self.texts_to_show.append(self.effects_volume_text_indicator)
        self.effects_volume_input = BaseInputText(text = str(int(self.effects_volume*100)),width=config.WINDOW_WIDTH * 0.065625, height=config.WINDOW_HEIGHT * 0.075 ,font_size = 21, base_color= self.game_color)
        self.uimanager.add(self.effects_volume_input)


        self.save_volume_preferences_button = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.13125, when_clicked=self.on_click_save_volume_preferences)
        self.prepare_button(self.save_volume_preferences_button)

    def update_layout(self):
        self.title_text.x = self.window.width * 0.5
        self.title_text.y = self.window.height * 0.9

        self.author_text.x = self.window.width * 0.5
        self.author_text.y = self.window.height * 0.825

        self.version_text.x = self.window.width * 0.5
        self.version_text.y = self.window.height * 0.80625

        self.back_button.center_x = self.window.width * 0.5
        self.back_button.center_y = self.window.height * 0.05


        self.game_color_text.x = self.window.width * 0.25
        self.game_color_text.y = self.window.height * 0.75

        self.game_color_red_input.center_x = self.window.width * 0.475
        self.game_color_red_input.center_y = self.window.height * 0.7375

        self.game_color_green_input.center_x = self.window.width * 0.575
        self.game_color_green_input.center_y = self.window.height * 0.7375

        self.game_color_blue_input.center_x = self.window.width * 0.675
        self.game_color_blue_input.center_y = self.window.height * 0.7375

        self.save_game_color_button.center_x = self.window.width * 0.825
        self.save_game_color_button.center_y = self.window.height * 0.7375


        self.player1_text_indicator.x = self.window.width * 0.1125
        self.player1_text_indicator.y = self.window.height * 0.65

        self.player1_name_input.center_x = self.window.width * 0.275
        self.player1_name_input.center_y = self.window.height * 0.6375

        self.player1_color_red_input.center_x = self.window.width * 0.475
        self.player1_color_red_input.center_y = self.window.height * 0.6375

        self.player1_color_green_input.center_x = self.window.width * 0.575
        self.player1_color_green_input.center_y = self.window.height * 0.6375

        self.player1_color_blue_input.center_x = self.window.width * 0.675
        self.player1_color_blue_input.center_y = self.window.height * 0.6375

        self.save_player1_button.center_x = self.window.width * 0.825
        self.save_player1_button.center_y = self.window.height * 0.6375

        
        self.player2_text_indicator.x = self.window.width * 0.1125
        self.player2_text_indicator.y = self.window.height * 0.55

        self.player2_name_input.center_x = self.window.width * 0.275
        self.player2_name_input.center_y = self.window.height * 0.5375

        self.player2_color_red_input.center_x = self.window.width * 0.475
        self.player2_color_red_input.center_y = self.window.height * 0.5375

        self.player2_color_green_input.center_x = self.window.width * 0.575
        self.player2_color_green_input.center_y = self.window.height * 0.5375

        self.player2_color_blue_input.center_x = self.window.width * 0.675
        self.player2_color_blue_input.center_y = self.window.height * 0.5375

        self.save_player2_button.center_x = self.window.width * 0.825
        self.save_player2_button.center_y = self.window.height * 0.5375

        
        self.player3_text_indicator.x = self.window.width * 0.1125
        self.player3_text_indicator.y = self.window.height * 0.45

        self.player3_name_input.center_x = self.window.width * 0.275
        self.player3_name_input.center_y = self.window.height * 0.4375  
        self.player3_color_red_input.center_x = self.window.width * 0.475
        self.player3_color_red_input.center_y = self.window.height * 0.4375

        self.player3_color_green_input.center_x = self.window.width * 0.575
        self.player3_color_green_input.center_y = self.window.height * 0.4375   
        self.player3_color_blue_input.center_x = self.window.width * 0.675
        self.player3_color_blue_input.center_y = self.window.height * 0.4375

        self.save_player3_button.center_x = self.window.width * 0.825
        self.save_player3_button.center_y = self.window.height * 0.4375


        self.player4_text_indicator.x = self.window.width * 0.1125
        self.player4_text_indicator.y = self.window.height * 0.35

        self.player4_name_input.center_x = self.window.width * 0.275
        self.player4_name_input.center_y = self.window.height * 0.3375  
        self.player4_color_red_input.center_x = self.window.width * 0.475
        self.player4_color_red_input.center_y = self.window.height * 0.3375

        self.player4_color_green_input.center_x = self.window.width * 0.575
        self.player4_color_green_input.center_y = self.window.height * 0.3375   
        self.player4_color_blue_input.center_x = self.window.width * 0.675
        self.player4_color_blue_input.center_y = self.window.height * 0.3375

        self.save_player4_button.center_x = self.window.width * 0.825
        self.save_player4_button.center_y = self.window.height * 0.3375


        self.volume_text_indicator.x = self.window.width * 0.5
        self.volume_text_indicator.y = self.window.height * 0.25

        self.ui_volume_text_indicator.x = self.window.width * 0.25
        self.ui_volume_text_indicator.y = self.window.height * 0.175
        self.ui_volume_input.center_x = self.window.width * 0.35
        self.ui_volume_input.center_y = self.window.height * 0.1725

        self.effects_volume_text_indicator.x = self.window.width * 0.5
        self.effects_volume_text_indicator.y = self.window.height * 0.175
        self.effects_volume_input.center_x = self.window.width * 0.6
        self.effects_volume_input.center_y = self.window.height * 0.1725

        self.save_volume_preferences_button.center_x = self.window.width * 0.75
        self.save_volume_preferences_button.center_y = self.window.height * 0.1725

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

    def on_click_save_game_color(self, event: arcade.gui.UIOnClickEvent):
        print("save_game_color_button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_game_color(self.game_color_red_input, self.game_color_green_input, self.game_color_blue_input)

    def save_player_settings(self, 
                             playername_key: str,
                             player_name_input: BaseInputText,
                             user_color_key: str,
                             red_color_input: BaseInputText,
                             green_color_input: BaseInputText,
                             blue_color_input: BaseInputText
                             ):
        print(f"Saving settings for {playername_key}")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_player(
            name_requester=player_name_input,
            name_key=playername_key,
            red_requester=red_color_input,
            green_requester=green_color_input,
            blue_requester=blue_color_input,
            color_key=user_color_key
        )

    def on_click_save_player1(self, event: arcade.gui.UIOnClickEvent):
        print("save_player1_button clicked.")
        self.save_player_settings("player1_name", self.player1_name_input, "player1_color", self.player1_color_red_input, self.player1_color_green_input, self.player1_color_blue_input)

    def on_click_save_player2(self, event: arcade.gui.UIOnClickEvent):
        print("save_player2_button clicked.")
        self.save_player_settings("player2_name", self.player2_name_input, "player2_color", self.player2_color_red_input, self.player2_color_green_input, self.player2_color_blue_input)

    def on_click_save_player3(self, event: arcade.gui.UIOnClickEvent):
        print("save_player3_button clicked.")
        self.save_player_settings("player3_name", self.player3_name_input, "player3_color", self.player3_color_red_input, self.player3_color_green_input, self.player3_color_blue_input)

    def on_click_save_player4(self, event: arcade.gui.UIOnClickEvent):
        print("save_player4_button clicked.")
        self.save_player_settings("player4_name", self.player4_name_input, "player4_color", self.player4_color_red_input, self.player4_color_green_input, self.player4_color_blue_input)

    def on_click_save_volume_preferences(self, event: arcade.gui.UIOnClickEvent):
        print("save_volume_preferences_button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_volume_to(self.ui_volume_input, self.effects_volume_input)