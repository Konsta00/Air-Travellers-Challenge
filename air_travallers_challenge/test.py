from game import Game
from game import Player
from game import Questions

def print_options():
    print('''
[OPTIONS]
5. Display a clue ($TBD)
6. Use a powerup 
    ''')

# CREATE GAME, PLAYER ETC. SET NEEDED VARIABLES
input_name = 'test_name'
game = Game()
game.print_avatars()
input_avatar = 1
player = Player(input_name, input_avatar)
player.set_starting_airport(player.avatar_id)
game.set_player(player)
game.set_current_airport()
game.set_closest_airports()
questions = Questions()
questions.set_questions(player.avatar_id)


# ASK PLAYER A QUESTION. GET RANDOM QUESTION 
question = questions.return_random_question()

print_options()

reversed_questions_bool = questions.ask_question(question)

input_answer = int(input('Select correct answer by typing the corresponding number: '))

if input_answer:
    if reversed_questions_bool and input_answer == 1:
        print('CORRECT ANSWER \n 100 points added for player. \n $100 dollars added to players wallet.')
    elif reversed_questions_bool == False and input_answer == 2:
        print('CORRECT ANSWER \n 100 added points for player. \n $100 dollars added to players wallet.')
    else:
        print('WRONG ANSWER.')
        


# print('OLD VALUES: \n')
# player.print_player()

# # PRINT LIST OF AIRPORS WHERE PLAYER CAN TRAVEL
# print('TRAVEL TO A NEW AIRPORT')
# last_index = None
# for i, airport in enumerate(game.closest_airports):
#       print(f'{i+1}. {airport["name"]} | {airport["ident"]} ')
#       last_index = i

# # TODO: CREATE TRY STATEMENT FOR USER INPUT & MOVE THIS TO ACCORDING MODULE MAYBE

# # ASK USER TO SELECT AIRPORT
# selected_airport = int(input(f'SELECT AIRPORT BY TYPING 1-{last_index}: \n'))

# # "TRAVEL" TO NEW AIRPORT
# for i, airport in enumerate(game.closest_airports):
#     if i+1 == selected_airport:
#         game.current_airport = airport['ident']
#         player.airport = airport['ident']

print('NEW VALUES: \n')
player.print_player()

# print(game.closest_airports)

