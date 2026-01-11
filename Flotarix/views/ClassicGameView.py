import arcade
from base.BaseView import BaseView
from utils import assets_utils
from config import config
from utils import user_utils
from core.Spaceship import Spaceship
from core.Player import Player
from core.GameMap import Board
from base.BaseText import BaseText

class ClassicGameView(BaseView):
    def __init__(self, player_quantity: int = 2):
        super().__init__()

        self.secondary_game_color = self.game_color
        if user_utils.is_light(self.game_color):
            self.secondary_game_color = user_utils.adjust(self.game_color, -96)
        elif not(user_utils.is_light(self.game_color)):
            self.secondary_game_color = user_utils.adjust(self.game_color, +96)
        else:
            print("UNKNOW ERROR: tried processing self.secondary_game_color")

        self.fleets_start = user_utils.load_user_fleets()

        self.players = []

        for i in range(player_quantity):
            player_name = self.settings.get(f"player{i+1}_name", f"Player {i+1}")
            player_color = getattr(self, f"player{i+1}_color")
            player = Player(name=player_name, player_color=tuple(player_color))
            self.players.append(player)


        self.ships = []
        self.ship_sprites = arcade.SpriteList()

        for i in range(len(self.players)):
            fleet = self.fleets_start.get(f"player{i+1}", {})
            flagship_name = fleet.get("flagship", "unknow")
            recipe = assets_utils.load_ship_recipe("flagship", flagship_name)
            ship = Spaceship(
                recipe,
                player=self.settings.get(f"player{i+1}_name", f"Player {i+1}"),
                player_color=self.players[i].player_color,
                x_location=fleet.get("position", [0, 0])[0],
                y_location=fleet.get("position", [0, 0])[1]
            )
            self.ships.append(ship)
            self.ship_sprites.append(ship.sprite)

        self.board = Board(config.BOARD_XSIZE, config.BOARD_YSIZE)

        for ship in self.ships:
            square = self.board.get_square(ship.x_location, ship.y_location)
            if square:
                square.ship_inside = ship

        self.selected_ship = None
        self.selected_ship_sprite = None
        self.selected_ship_sprite_list = arcade.SpriteList()

        self.selected_ship_name = BaseText(text="", font_size=12)
        self.selected_ship_player = BaseText(text="", font_size=12)
        self.selected_ship_hp = BaseText(text="", font_size=12)
        self.texts_to_show.append(self.selected_ship_name)
        self.texts_to_show.append(self.selected_ship_player)
        self.texts_to_show.append(self.selected_ship_hp)


    def update_layout(self):
        super().update_layout()
        self.selected_ship_name.x = self.window.width * 0.055
        self.selected_ship_name.y = self.window.height * 0.825
        self.selected_ship_player.x = self.window.width * 0.055
        self.selected_ship_player.y = self.window.height * 0.7938
        self.selected_ship_hp.x = self.window.width * 0.055
        self.selected_ship_hp.y = self.window.height * 0.7625

    def on_draw(self):
        super().on_draw()
        self.draw_board()
        self.uimanager.draw()
        self.selected_ship_sprite_list.draw()
        self.draw_selected_ship_info()


    def on_resize(self, width, height):
        super().on_resize(width, height)

    def on_show_view(self):
        super().on_show_view()

    def calculate_board_origin(self):
        total_width = config.BOARD_XSIZE * config.SQUARE_SIZE
        total_height = config.BOARD_YSIZE * config.SQUARE_SIZE

        origin_x = (self.window.width - total_width) / 2
        origin_y = (self.window.height - total_height) / 2
        return origin_x, origin_y

    def draw_board(self):
        origin_x, origin_y = self.calculate_board_origin()

        for y in range(config.BOARD_YSIZE):
            for x in range(config.BOARD_XSIZE):
                left   = origin_x + x * config.SQUARE_SIZE
                bottom = origin_y + y * config.SQUARE_SIZE

                if (x + y) % 2 == 0:
                    color = self.game_color
                else:
                    color = self.secondary_game_color

                arcade.draw_lbwh_rectangle_filled(
                    left,
                    bottom,
                    config.SQUARE_SIZE,
                    config.SQUARE_SIZE,
                    color
                )

        for ship in self.ships:
            ship.sprite.center_x = origin_x + ship.x_location * config.SQUARE_SIZE + config.SQUARE_SIZE / 2
            ship.sprite.center_y = origin_y + ship.y_location * config.SQUARE_SIZE + config.SQUARE_SIZE / 2

        self.ship_sprites.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        origin_x, origin_y = self.calculate_board_origin()

        board_x = int((x - origin_x) // config.SQUARE_SIZE)
        board_y = int((y - origin_y) // config.SQUARE_SIZE)

        square = self.board.get_square(board_x, board_y)

        if square and square.ship_inside:
            self.selected_ship = square.ship_inside

            hud_sprite = arcade.Sprite()
            hud_sprite.texture = self.selected_ship.sprite.texture
            hud_sprite.scale = 0.084  # miniatura
            hud_sprite.center_x = self.window.width * 0.06375
            hud_sprite.center_y = self.window.height * 0.925

            self.selected_ship_sprite_list.clear()
            self.selected_ship_sprite_list.append(hud_sprite)
            self.selected_ship_sprite = hud_sprite

            print(f"Ship: {self.selected_ship.name} selected at ({board_x}, {board_y}) from player {self.selected_ship.player}")
            self.update_layout()
        else:
            # No hay nave seleccionada
            self.selected_ship = None
            self.selected_ship_sprite_list.clear()
            print("Click sin nave")


    def draw_selected_ship_info(self):
        if self.selected_ship is None:
            self.selected_ship_name.text = ""
            self.selected_ship_player.text = ""
            self.selected_ship_hp.text = ""
            return

        self.selected_ship_name.text = f"{self.selected_ship.name}"
        self.selected_ship_player.text = f"{self.selected_ship.player}"
        self.selected_ship_hp.text = f"{self.selected_ship.current_hp} / {self.selected_ship.hp_pool}"

