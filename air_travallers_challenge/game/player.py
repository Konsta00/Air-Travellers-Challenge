import random
import json
from database.db_models import insert_player_sql 
from database.db_models import get_airports_iso_sql
from database.db_models import update_points

class Player:
    def __init__(self, name, avatar_id):
        self.id = None
        self.name = name
        self.airport = None
        self.budget = 10000
        self.distance_traveled = 0
        self.avatar_id = avatar_id
        self.co2_consumed = 0
        self.points = 0
        self.powerups = ('skip_question', 'skip_question', 'skip_question', 'random_reward')
        self.total_questions_answered = 0
        self.current_answered = 0

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

# AIRPORTS DICTIONARY
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

            try:
                self.id =  insert_player_sql(params)
                print(self.id)
            except Exception as error:
                print('Error inserting player to database: {error}')


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

        self.distance_travelled += distance
        self.airport = new_airport
        self.co2_consumed += amount_co2_consumed

        self.update_database()

    def check_values(self, game):
        if self.budget < 0:
            self.budget = 0
        if self.points < 0:
            self.points = 0
        if self.points >= 1000:
            game.game_over = True

    def update_budget(self, amount):
        if bool(amount):
            self.budget += amount
        elif not bool(amount):
            self.budget -= amount

# DONE: UPDATE PLAYER POINTS
    def update_points(self, points_to_add):
        if bool(points_to_add):
            self.points += points_to_add
        elif not bool(points_to_add):
            self.points -= points_to_add
            if self.points < 0: self.points = 0

# DONE: UPDATE CO2 REDUCTION
    def update_co2_emissions(self, co2_reduction):
        self.co2_consumed -= co2_reduction
        print(f"CO2 emission reduced by {co2_reduction} kg. Current CO2 emission: {self.co2_consumed} kg.")

    def update_distance(self, distance_to_add):
        if bool(distance_to_add):
            self.distance += distance_to_add
        else:
            self.distance -= distance_to_add

# TODO: SELECT RANDOM POWERUP AND AND IT TO PLAYER INSTANCE DICTIONARY
    def random_powerup(self):
        power_ups = ('skip_question', 'random_reward')
        random_choice = random.choice(list(power_ups))
        self.powerups += (random_choice,)

    def use_powerup(self, powerup):
        if powerup == 'random_reward':
            random_num = random.randint(0, 15)
            if random_num < 2:
                self.budget += 200
            elif random_num >2 and random_num < 6:
                self.budget += 150
            else:
                self.budget += 100
            return 1
        elif powerup == 'skip_question':
            return 2
        elif powerup == 'random_powerup':
            return 3
        
    def use_question_powerup(self, powerup):
        for powerup in self.powerups:
            pass

    def update_questions(self):
        self.total_questions_answered += 1
        self.current_answered += 1