from game import Game
from game import Player

input_name = 'test_name'

game = Game()

game.print_avatars()
input_avatar = 1

player = Player(input_name, input_avatar)
game.set_player(player)

player.set_starting_airport(player.avatar_id)
game.set_current_airport()
 
game.set_closest_airports()
print(game.closest_airports)

print('OLD VALUES: \n')
print(f'Player name: {player.name}')
print(f'Player avatar: {player.avatar_id}')
print(f'Player current airport: {player.airport}')

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
print(f'Player name: {player.name}')
print(f'Player avatar: {player.avatar_id}')
print(f'Player current airport: {player.airport}')

# print(game.closest_airports)