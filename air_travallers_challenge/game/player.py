import random
import json
from database.db_models import insert_player_sql 
from database.db_models import get_airports_iso_sql

class Player:
    def __init__(self, name, avatar_id):
        self.id = None
        self.name = name
        self.airport = None
        self.budget = 500
        self.distance_traveled = 0
        self.avatar_id = avatar_id
        self.co2_consumed = 0
        self.points = 0
        self.powerups = (
        )

    def print_player(self):
        print('ID: ', self.id)
        print('Name: ', self.name)
        print('Points: ', self.points)
        print('Budget: ', self.budget)
        print('Airport: ', self.airport)
        print('Co2 consumed: ', self.co2_consumed)
        print('Avatar ID: ', self.avatar_id)

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

            self.id =  insert_player_sql(params)
            print(self.id)


# TODO: UPDATE PLAYER INFO TO DABASE ALMOST EVERYTIME SOMETHING GETS CHANGED
    def update_database(self):
        print(f'''
        NEW PLAYER VALUES FROM update_database(): 
            \n ID: {self.id}
            \n Name: {self.name}
            \n Points: {self.points}
            \n Budget: {self.budget} 
            \n Distance traveled: {self.distance_travelled}
            \n Co2 consumed: {self.co2_consumed}
        ''')

# TODO: UPDATE PLAYER
    def update_player(self, points, amount, distance, new_airport, amount_co2_consumed):
        
        print(f'''
        OLD PLAYER VALUES: 
            \n ID: {self.id}
            \n Name: {self.name}
            \n Points: {self.points}
            \n Budget: {self.budget} 
            \n Distance traveled: {self.distance_travelled}
            \n Co2 consumed: {self.co2_consumed}
        ''')

        if bool(points):
            self.points += points
        else:
            self.points -= points
        
        if bool(amount):
            self.budget += amount
        else:
            self.budget -= amount

        self.distance_travelled += + distance
        self.airport = new_airport
        self.co2_consumed += co2_consumed

        self.update_database()



# TODO: UPDATE PLAYER POINTS
    def update_points(points_to_add):
        var = "var"


# TODO: SELECT RANDOM POWERUP AND AND IT TO PLAYER INSTANCE DICTIONARY
    def random_powerup():
        asd = 'asd'