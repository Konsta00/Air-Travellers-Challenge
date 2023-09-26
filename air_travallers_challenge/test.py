from game import Game
from game import Player
from game import Questions

input_name = 'test_name'

game = Game()

game.print_avatars()
input_avatar = 1

player = Player(input_name, input_avatar)
player.set_starting_airport(player.avatar_id)

game.set_player(player)
game.set_current_airport()
game.set_closest_airports()

# print(game.closest_airports)

# ASK A QUESTION

questions = Questions()
questions.set_questions(player.avatar_id)

print(questions.questions)


print('OLD VALUES: \n')
player.print_player()

# PRINT LIST OF AIRPORS WHERE PLAYER CAN TRAVEL
print('TRAVEL TO A NEW AIRPORT')
last_index = None
for i, airport in enumerate(game.closest_airports):
      print(f'{i+1}. {airport["name"]} | {airport["ident"]} ')
      last_index = i


# TODO: CREATE TRY STATEMENT FOR USER INPUT & MOVE THIS TO ACCORDING MODULE MAYBE

# ASK USER TO SELECT AIRPORT
selected_airport = int(input(f'SELECT AIRPORT BY TYPING 1-{last_index}: \n'))

# "TRAVEL" TO NEW AIRPORT
for i, airport in enumerate(game.closest_airports):
    if i+1 == selected_airport:
        game.current_airport = airport['ident']
        player.airport = airport['ident']

print('NEW VALUES: \n')
player.print_player()

# print(game.closest_airports)