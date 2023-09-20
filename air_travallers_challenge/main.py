from game import Game
from game import Player

new_player = Player('Konsta', 'Velho')
new_game = Game()

new_game.set_player(new_player)

print(new_game)