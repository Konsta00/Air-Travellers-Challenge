import random
from player import Player 

class Game:
    def __init__(self, airports):
        self.airports = airports
        self.player = None
        self.current_airport = None

    def set_player(self, player):
        self.player = player

    
