import random
# from player import Player 
from database.db_models import get_closest_airports

class Game:
    def __init__(self):
        self.closest_airports = None
        self.player = None
        self.current_airport = None

    def set_player(self, player):
        self.player = player

    def set_current_airport(self):
        self.current_airport = self.player.current_airport

    def set_closest_airports(self):
        self.closest_airports = get_closest_airports(self.current_airport)
    
