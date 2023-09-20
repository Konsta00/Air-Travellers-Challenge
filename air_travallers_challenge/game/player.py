import random

class Player:
    def __init__(self, name, character):
        self.name = name
        self.airport = None
        self.budget = 500
        self.distance_traveled = 0
        self.character = character


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