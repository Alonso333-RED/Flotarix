import arcade
import arcade.gui
from utils import user_utils
from utils import assets_utils

class BaseView(arcade.View):
    def __init__(self):
        super().__init__()
        self.settings = user_utils.load_user_settings()
        self.ui_volume = self.settings.get("ui_volume", 1.0)
        self.background_color = self.settings["game_color"]
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=15)

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.anchor_layout.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y",
            align_y = 0,
            align_x = 0
        )
        self.uimanager.add(self.anchor_layout)

        self.texts_to_show = []

    def on_draw(self):
        self.clear()
        self.uimanager.draw()
        self.show_texts(self.texts_to_show)

    def on_click_default(self, event: arcade.gui.UIOnClickEvent):
        print("default response to button clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)

    def prepare_button(self, button: arcade.gui.UIFlatButton, v_box: arcade.gui.UIBoxLayout = None): # type: ignore
        if v_box is not None:
            v_box.add(button)
        self.uimanager.add(button)

    def show_texts(self, list: list):
        self.texts_to_show = list
        for text in self.texts_to_show:
            text.draw()
