import arcade
from base.BaseView import BaseView
from utils import assets_utils
from config import config
from utils import user_utils
from core.Spaceship import Spaceship
from core.Player import Player
from core.GameMap import Board

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
            player = Player(name=player_name, team_color=tuple(player_color))
            self.players.append(player)


        self.ships = []
        self.ship_sprites = arcade.SpriteList()

        for i in range(len(self.players)):
            fleet = self.fleets_start.get(f"player{i+1}", {})
            flagship_name = fleet.get("flagship", "unknow")
            recipe = assets_utils.load_ship_recipe(flagship_name)
            ship = Spaceship(
                recipe,
                team="player",
                team_color=self.players[i].team_color,
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
        clicked_ships = arcade.get_sprites_at_point((x, y), self.ship_sprites)
        print("Click")

        if clicked_ships:
            ship_sprite = clicked_ships[0]
            print("¡Click en nave!")
            self.selected_ship = ship_sprite
        else:
            print("Click sin nave")
            self.selected_ship = None
