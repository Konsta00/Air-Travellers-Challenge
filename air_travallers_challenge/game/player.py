import random
from database.db_models import insert_player_sql 


class Player:
    def __init__(self, name, character):
        self.name = name
        self.airport = None
        self.budget = 500
        self.distance_traveled = 0
        self.character = character
        self.co2_consumed = 0


    def set_starting_airport(self):
        starting_airports = {
                "KATL": "Hartsfield-Jackson Atlanta International Airport, USA",
                "ZBAA": "Beijing Capital International Airport, China",
                "EGLL": "London Heathrow Airport, UK",
                "LFPG": "Paris Charles de Gaulle Airport, France",
                "RJTT": "Tokyo Haneda Airport, Japan",
                "CYYZ": "Toronto Pearson International Airport, Canada",
                "OMDB": "Dubai International Airport, UAE",
                "EDDF": "Frankfurt Airport, Germany",
                "RKSI": "Incheon International Airport, South Korea",
                "KLAX": "Los Angeles International Airport, USA",
            }
        
        random_airport = random.choice(list(starting_airports.keys()))
        self.airport = random_airport

    def update_airport(self, airport):
        self.airport = airport

    def insert_player_to_database(self):
            name = self.name
            character = self.character
            budget = self.budget
            distance = self.distance_traveled
            current_airport = self.airport
            co2_consumed = self.co2_consumed

            insert_player_sql(name, current_airport, character, budget, co2_consumed)

    def update_database(self):
        asd = 'asd'
