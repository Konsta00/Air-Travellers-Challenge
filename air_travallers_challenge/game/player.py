import random
import json
from database.db_models import insert_player_sql 
from database.db_models import get_airports_iso_sql

class Player:
    def __init__(self, name, avatar_id):
        self.name = name
        self.airport = None
        self.budget = 500
        self.distance_traveled = 0
        self.avatar_id = avatar_id
        self.co2_consumed = 0
        self.points = 0
        self.powerups = (
        )

# GET ALL AIRPORTS FROM SELECTED AVATAR AND SET STARTING AIRPORT FOR PLAYER 
    def set_starting_airport(self, avatar_id):
        iso = ''

        if avatar_id == 1:
            # avatar_id = 1 = Donald Trump
            iso = 'US'
        elif avatar_id == 2:
            # avatar_id = 2 = Mona Lisa
            iso = 'FR'
        elif avatar_id == 3:
            # avatar_id = 3 = Felipe IV
            iso = 'ES'


        airports_dict = {}
        
        airports = get_airports_iso_sql(iso)

        for airport in airports:
            airports_dict[f'{airport["ident"]}'] = f'{airport["name"]}'

        starting_airport = random.choice(list(airports_dict.keys()))
        self.airport = starting_airport
        

# UPDATE PLAYERS AIRPORT TO CURRENT AIRPORT[ GETS PASSED IN AS A PARAMETER ]
    def update_airport(self, airport):
        self.airport = airport

# INSERT PLAYER INTO DATABASE
    def insert_player_to_database(self):
            params = (
                        self.name,
                        self.avatar_id,
                        self.budget,
                        self.distance_traveled,
                        self.airport,
                        self.co2_consumed
                    )

            insert_player_sql(params)

# TODO: UPDATE PLAYER INFO TO DABASE ALMOST EVERYTIME SOMETHING GETS CHANGED
    def update_database(self):
        asd = 'asd'


# TODO: UPDATE PLAYER POINTS
    def update_points(points_to_add):
        var = "var"


# TODO: SELECT RANDOM POWERUP AND AND IT TO PLAYER INSTANCE DICTIONARY
    def random_powerup():
        asd = 'asd'