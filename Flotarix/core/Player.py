class Player:
    def __init__ (self, name: str, team_color: tuple, money: int = 25):
        self.name = name
        self.team_color = team_color
        self.score = 0
        self.money = money