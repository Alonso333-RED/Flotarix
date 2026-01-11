from utils import assets_utils
from config import config

class SpaceshipRecipe:
    def __init__(self, category: str, data: dict):
        self.name = data["name"]
        self.category = category
        self.cost = data["cost"]
        self.cooldown = data["cooldown"]
        self.movement = data["movement"]
        self.hp_pool = data["hp_pool"]
        self.attack = data["attack"]
        self.sprite = assets_utils.load_ship_sprite(category, self.name, 0.048)


class Spaceship:
    def __init__(self, recipe: SpaceshipRecipe, player: str, player_color: tuple, x_location: int, y_location: int):
        self.name = recipe.name
        self.category = recipe.category
        self.recipe = recipe
        self.player = player
        self.player_color = player_color
        self.x_location = x_location
        self.y_location = y_location
        self.hp_pool = recipe.hp_pool
        self.current_hp = recipe.hp_pool
        self.attack = recipe.attack
        self.movement = recipe.movement
        self.sprite  = assets_utils.load_ship_sprite(self.category, self.name, 0.048, (self.player_color[0], self.player_color[1], self.player_color[2], 0.75))

    def update_sprite_position(self, origin_x, origin_y):
        self.sprite.center_x = origin_x + self.x_location * config.SQUARE_SIZE + config.SQUARE_SIZE / 2
        self.sprite.center_y = origin_y + self.y_location * config.SQUARE_SIZE + config.SQUARE_SIZE / 2
