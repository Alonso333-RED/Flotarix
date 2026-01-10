class Player:
    def __init__ (self, name: str, player_color: tuple, money: int = 25):
        self.name = name
        self.player_color = player_color
        self.score = 0
        self.money = money