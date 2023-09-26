import random
# from player import Player 
from database.db_models import get_closest_airports

class Game:
# INIATIALIZE GAME CLASS 
    def __init__(self):
        self.game_over = False
        self.closest_airports = None
        self.player = None
        self.current_airport = None

# SET GAME INSTANCE PLAYER
    def set_player(self, player):
        self.player = player

# SET GAME CURRENT AIRPORT TO PLAYER AIRPORT (CURRENT)
    def set_current_airport(self):
        self.current_airport = self.player.airport

# SET 10 CLOSEST AIRPORT TO GAME FROM DATABASE QUERY 
    def set_closest_airports(self):
        self.closest_airports = get_closest_airports(self.current_airport)

# PRINT AVATARS ON SCREEN
    def print_avatars(self):
        avatars = ('Donald Trump', 'Mona Lisa', 'Felipe VI')

        index = 1
        print(f'Select avatar from {index}-{len(avatars)}: ')
        for index, avatar in enumerate(avatars):
            print(f'{index+1}. {avatar}')

# UPDATE GAME WITH NEW VALUES
    def update_game(self, status, player, next_airport, next_closest_airports):
        self.game_over = status
        self.current_airport = next_airport
        self.closest_airports = next_closest_airports
