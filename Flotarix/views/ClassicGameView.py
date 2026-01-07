import arcade
from base.BaseView import BaseView
from utils import assets_utils
from config import config
from utils import user_utils
from core.Spaceship import Spaceship

class ClassicGameView(BaseView):
    def __init__(self, player1: bool, player2: bool, player3: bool, player4: bool):
        super().__init__()

        self.secondary_game_color = self.game_color
        if user_utils.is_light(self.game_color):
            self.secondary_game_color = user_utils.adjust(self.game_color, -96)
        elif not(user_utils.is_light(self.game_color)):
            self.secondary_game_color = user_utils.adjust(self.game_color, +96)
        else:
            print("UNKNOW ERROR: tried processing self.secondary_game_color")

        self.ships = []
        self.ship_sprites = arcade.SpriteList()

        recipe = assets_utils.load_ship_recipe("Andromeda")
        ship = Spaceship(recipe, team="player", team_color=self.player1_color, x_location=5, y_location=10)
        self.ships.append(ship)
        self.ship_sprites.append(ship.image)

        recipe = assets_utils.load_ship_recipe("Jupiter")
        ship = Spaceship(recipe, team="player", team_color=self.player2_color, x_location=5, y_location=0)
        self.ships.append(ship)
        self.ship_sprites.append(ship.image)

        recipe = assets_utils.load_ship_recipe("Andromeda")
        ship = Spaceship(recipe, team="player", team_color=self.player3_color, x_location=0, y_location=5)
        self.ships.append(ship)
        self.ship_sprites.append(ship.image)

        recipe = assets_utils.load_ship_recipe("Jupiter")
        ship = Spaceship(recipe, team="player", team_color=self.player4_color, x_location=10, y_location=5)
        self.ships.append(ship)
        self.ship_sprites.append(ship.image)

    def update_layout(self):
        pass

    def on_draw(self):
        super().on_draw()
        self.draw_board()
        self.uimanager.draw()

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

        # 1) Dibujar el tablero
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

        # 2) Actualizar posición de cada nave
        for ship in self.ships:
            ship.image.center_x = origin_x + ship.x_location * config.SQUARE_SIZE + config.SQUARE_SIZE / 2
            ship.image.center_y = origin_y + ship.y_location * config.SQUARE_SIZE + config.SQUARE_SIZE / 2

        # 3) Dibujar todos los sprites
        self.ship_sprites.draw()
