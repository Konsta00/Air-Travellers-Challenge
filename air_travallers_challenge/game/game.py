import random
# from player import Player 
from database.db_models import get_closest_airports
from database.db_models import calculate_co2_used


class Game:
    def __init__(self):
        self.game_over = False
        self.closest_airports = None
        self.player = None
        self.current_airport = None
        self.old_airport = None

# SET GAME INSTANCE PLAYER
    def set_player(self, player):
        self.player = player

# SET GAME CURRENT AIRPORT TO PLAYER AIRPORT (CURRENT)
    def set_current_airport(self):
        self.current_airport = self.player.airport

# SET 10 CLOSEST AIRPORT TO GAME FROM DATABASE QUERY 
    def load_closest_airports(self):
        self.closest_airports = get_closest_airports(self.current_airport)

    def print_available_airports(self):
        print('Select from the airports to which you want to travel to.')
        for i, airport in enumerate(self.closest_airports, start=0):
            print(f'{"CURRENT AIRPORT:" if i == 0 else f"{i}."} {airport["name"]} | {airport["ident"]}')

# PRINT AVATARS ON SCREEN 
    def display_avatars(self):
        avatars = ('Donald Trump', 'Mona Lisa', 'Felipe VI')
        for index, avatar in enumerate(avatars, start=1):
            print(f'{index}. {avatar}')

# UPDATE GAME WITH NEW VALUES
    def update_game(self):
        # GET CLOSEST AIRPORTS 
        old = self.old_airport
        new = self.current_airport

# CALCULATE AND UPDATE PLAYER CO2 CONSUMED
        co2_used = calculate_co2_used(old, new)
        self.player.co2_consumed += co2_used

# CHANGE GAME INSTANCE & PLAYER INSTANCE AIRPORT TO NEW AIRPORT BASED ON PLAYER INPUT 
    def travel_to_new_airport(self, input_airport):
        for i, airport in enumerate(self.closest_airports):
            if i == input_airport:
                self.old_airport = self.current_airport
                self.current_airport = airport['ident']
                self.player.airport = airport['ident']
                self.load_closest_airports()

    def display_options(self):
        print("\n╔══════════════════════════╗\n  Air Travellers Challenge\n╚══════════════════════════╝\n")
        print(f'''
              [PLAYER {self.player.name.upper()}]:\n
                Points: {self.player.points} points 
                Budged: {self.player.budget}€
                Co2 consumed: {self.player.co2_consumed}

              WHAT DO YOU WANT TO DO:
                1. ANSWER ANOTHER QUESTION
                2. TRAVEL TO NEW AIRPORT
                3. VISIT THE STORE
            ''')
        
    def travel(self):
        try:
            input_airport = int(input(f'SELECT AIRPORT BY TYPING 1-{len(self.closest_airports)-1}:'))
            if 1 <= input_airport <= len(self.closest_airports) - 1:
                self.travel_to_new_airport(input_airport)
            else:
                print('Invalid airport selection.')
        except ValueError:
            print('Invalid input. Please enter a valid airport number.')


