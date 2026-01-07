from utils import assets_utils
from config import config

class SpaceshipRecipe:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.cost = data["cost"]
        self.cooldown = data["cooldown"]
        self.movement = data["movement"]
        self.hp_pool = data["hp_pool"]
        self.attack = data["attack"]
        self.image = assets_utils.load_ship_sprite(self.name, 0.048)


class Spaceship:
    def __init__(self, recipe: SpaceshipRecipe, team: str, team_color: tuple, x_location: int, y_location: int):
        self.name = recipe.name
        self.recipe = recipe
        self.team = team
        self.team_color = team_color
        self.x_location = x_location
        self.y_location = y_location
        self.hp_pool = recipe.hp_pool
        self.current_hp = recipe.hp_pool
        self.attack = recipe.attack
        self.movement = recipe.movement
        self.image  = assets_utils.load_ship_sprite(self.name, 0.048, (self.team_color[0], self.team_color[1], self.team_color[2], 0.75))

    def update_sprite_position(self, origin_x, origin_y):
        self.image.center_x = origin_x + self.x_location * config.SQUARE_SIZE + config.SQUARE_SIZE / 2
        self.image.center_y = origin_y + self.y_location * config.SQUARE_SIZE + config.SQUARE_SIZE / 2
