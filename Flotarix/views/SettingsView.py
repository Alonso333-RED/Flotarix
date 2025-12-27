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

        self.game_color_red_input = BaseInputText(text = str(self.game_colors[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.game_color_green_input = BaseInputText(text = str(self.game_colors[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.game_color_blue_input = BaseInputText(text = str(self.game_colors[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.game_color_red_input)
        self.uimanager.add(self.game_color_green_input)
        self.uimanager.add(self.game_color_blue_input)

        self.save_game_color = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_game_color)
        self.prepare_button(self.save_game_color)


        self.player1_text_indicator = BaseText(text="1: ",font_size=28)
        self.texts_to_show.append(self.player1_text_indicator)

        self.player1_name_input = BaseInputText(text = self.settings.get("username1", ""),width=config.WINDOW_WIDTH * 0.275, base_color=tuple(self.player1_color))
        self.player1_color_red_input = BaseInputText(text = str(self.player1_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.player1_color_green_input = BaseInputText(text = str(self.player1_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.player1_color_blue_input = BaseInputText(text = str(self.player1_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.player1_name_input)
        self.uimanager.add(self.player1_color_red_input)
        self.uimanager.add(self.player1_color_green_input)
        self.uimanager.add(self.player1_color_blue_input)

        self.save_player1_color = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_player1_color)
        self.prepare_button(self.save_player1_color)


        self.player2_text_indicator = BaseText(text="2: ",font_size=28)
        self.texts_to_show.append(self.player2_text_indicator)

        self.player2_name_input = BaseInputText(text = self.settings.get("username2", ""),width=config.WINDOW_WIDTH * 0.275, base_color=tuple(self.player2_color))
        self.player2_color_red_input = BaseInputText(text = str(self.player2_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.player2_color_green_input = BaseInputText(text = str(self.player2_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.player2_color_blue_input = BaseInputText(text = str(self.player2_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.player2_name_input)
        self.uimanager.add(self.player2_color_red_input)
        self.uimanager.add(self.player2_color_green_input)
        self.uimanager.add(self.player2_color_blue_input)

        self.save_player2_color = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_player2_color)
        self.prepare_button(self.save_player2_color)


        self.player3_text_indicator = BaseText(text="3: ",font_size=28)
        self.texts_to_show.append(self.player3_text_indicator)

        self.player3_name_input = BaseInputText(text = self.settings.get("username3", ""),width=config.WINDOW_WIDTH * 0.275, base_color=tuple(self.player3_color))
        self.player3_color_red_input = BaseInputText(text = str(self.player3_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.player3_color_green_input = BaseInputText(text = str(self.player3_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.player3_color_blue_input = BaseInputText(text = str(self.player3_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.player3_name_input)
        self.uimanager.add(self.player3_color_red_input)
        self.uimanager.add(self.player3_color_green_input)
        self.uimanager.add(self.player3_color_blue_input)

        self.save_player3_color = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_player3_color)
        self.prepare_button(self.save_player3_color)


        self.player4_text_indicator = BaseText(text="4: ",font_size=28)
        self.texts_to_show.append(self.player4_text_indicator)

        self.player4_name_input = BaseInputText(text = self.settings.get("username4", ""),width=config.WINDOW_WIDTH * 0.275, base_color=tuple(self.player4_color))
        self.player4_color_red_input = BaseInputText(text = str(self.player4_color[0]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([128, 0, 0]))
        self.player4_color_green_input = BaseInputText(text = str(self.player4_color[1]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 128, 0]))
        self.player4_color_blue_input = BaseInputText(text = str(self.player4_color[2]),width=config.WINDOW_WIDTH * 0.0875, base_color =tuple([0, 0, 128]))

        self.uimanager.add(self.player4_name_input)
        self.uimanager.add(self.player4_color_red_input)
        self.uimanager.add(self.player4_color_green_input)
        self.uimanager.add(self.player4_color_blue_input)

        self.save_player4_color = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.175, when_clicked=self.on_click_save_player4_color)
        self.prepare_button(self.save_player4_color)


        self.volume_text_indicator = BaseText(text="Volumen (0-100): ",font_size=28)
        self.texts_to_show.append(self.volume_text_indicator)

        self.ui_volume_text_indicator = BaseText(text="Interfaz: ",font_size=21)
        self.texts_to_show.append(self.ui_volume_text_indicator)
        self.ui_volume_input = BaseInputText(text = str(int(self.ui_volume*100)),width=config.WINDOW_WIDTH * 0.065625, height=config.WINDOW_HEIGHT * 0.075 ,font_size = 21, base_color= self.game_colors)
        self.uimanager.add(self.ui_volume_input)


        self.effects_volume_text_indicator = BaseText(text="Efectos: ",font_size=21)
        self.texts_to_show.append(self.effects_volume_text_indicator)
        self.effects_volume_input = BaseInputText(text = str(int(self.effects_volume*100)),width=config.WINDOW_WIDTH * 0.065625, height=config.WINDOW_HEIGHT * 0.075 ,font_size = 21, base_color= self.game_colors)
        self.uimanager.add(self.effects_volume_input)


        self.save_volume_preferences = BaseButton("Guardar", width = config.WINDOW_WIDTH * 0.13125, when_clicked=self.on_click_save_volume_preferences)
        self.prepare_button(self.save_volume_preferences)

    def on_draw(self):
        super().on_draw()

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

        self.save_game_color.center_x = self.window.width * 0.825
        self.save_game_color.center_y = self.window.height * 0.7375


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

        self.save_player1_color.center_x = self.window.width * 0.825
        self.save_player1_color.center_y = self.window.height * 0.6375

        
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

        self.save_player2_color.center_x = self.window.width * 0.825
        self.save_player2_color.center_y = self.window.height * 0.5375

        
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

        self.save_player3_color.center_x = self.window.width * 0.825
        self.save_player3_color.center_y = self.window.height * 0.4375


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

        self.save_player4_color.center_x = self.window.width * 0.825
        self.save_player4_color.center_y = self.window.height * 0.3375


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

        self.save_volume_preferences.center_x = self.window.width * 0.75
        self.save_volume_preferences.center_y = self.window.height * 0.1725

        

    def on_click_back(self, event: arcade.gui.UIOnClickEvent):
        print("response to back button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.MenuView import MenuView
        self.uimanager.clear()
        view = MenuView()
        self.window.show_view(view)

    def on_click_save_game_color(self, event: arcade.gui.UIOnClickEvent):
        print("response to save game color button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_colors_to(self.game_color_red_input, self.game_color_green_input, self.game_color_blue_input, "game_color")

    def on_click_save_player1_color(self, event: arcade.gui.UIOnClickEvent):
        print("response to save player 1 color button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_colors_to(self.player1_color_red_input, self.player1_color_green_input, self.player1_color_blue_input, "user1_color")
        user_utils.save_name_to(self.player1_name_input, "username1")

    def on_click_save_player2_color(self, event: arcade.gui.UIOnClickEvent):
        print("response to save player 2 color button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_colors_to(self.player2_color_red_input, self.player2_color_green_input, self.player2_color_blue_input, "user2_color")
        user_utils.save_name_to(self.player2_name_input, "username2")

    def on_click_save_player3_color(self, event: arcade.gui.UIOnClickEvent):
        print("response to save player 3 color button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_colors_to(self.player3_color_red_input, self.player3_color_green_input, self.player3_color_blue_input, "user3_color")
        user_utils.save_name_to(self.player3_name_input, "username3")

    def on_click_save_player4_color(self, event: arcade.gui.UIOnClickEvent):
        print("response to save player 4 color button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_colors_to(self.player4_color_red_input, self.player4_color_green_input, self.player4_color_blue_input, "user4_color")
        user_utils.save_name_to(self.player4_name_input, "username4")

    def on_click_save_volume_preferences(self, event: arcade.gui.UIOnClickEvent):
        print("response to save volume preferences button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        user_utils.save_volume_to(self.ui_volume_input, self.effects_volume_input)