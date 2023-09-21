from game import Game
from game import Player


# TODO: PRINT WELCOME SCREEN & RULES FOR THE GAME

print('''
   _____  .__         ___________                         .__  .__              /\       
  /  _  \ |__|______  \__    ___/___________ ___  __ ____ |  | |  |   __________)/ ______
 /  /_\  \|  \_  __ \   |    |  \_  __ \__  \\  \/ // __ \|  | |  | _/ __ \_  __ \/  ___/
/    |    \  ||  | \/   |    |   |  | \// __ \\   /\  ___/|  |_|  |_\  ___/|  | \/\___ \ 
\____|__  /__||__|      |____|   |__|  (____  /\_/  \___  >____/____/\___  >__|  /____  >
        \/                                  \/          \/               \/           \/ 
              _________ .__           .__  .__                                           
              \_   ___ \|  |__ _____  |  | |  |   ____   ____    ____   ____             
              /    \  \/|  |  \\__  \ |  | |  | _/ __ \ /    \  / ___\_/ __ \            
              \     \___|   Y  \/ __ \|  |_|  |_\  ___/|   |  \/ /_/  >  ___/            
               \______  /___|  (____  /____/____/\___  >___|  /\___  / \___  >           
                      \/     \/     \/               \/     \//_____/      \/            
      ''')

# ASK FOR NAME
input_name = str(input('Select a name for player: '))

# CREATE GAME INSTANCE
game = Game()

#PRINT CHARACTERS FOR USERkk TO SELECT
game.print_characters()

input_character = int(input())

# CRETE NEW PLAYER INSTANCE WITH INPUT_NAME AND INPUT_CHARACTER
player = Player(input_name, input_character)

# CREATE NEW PLAYER IN DATABASE
player.insert_player_to_database()

# SET PLAYER IN GAME INSTANCE
game.set_player(player)

# SET AIPORT TO PLAYER & CURRENT AIRPORT TO GAME
player.set_starting_airport()
game.set_current_airport() 

# SET CLOSEST AIRPORTS TO GAME
game.set_closest_airports()


# DEBUG & DEVELOPEMENT

print(f'Player name: {player.name}')
print(f'Player character: {player.character}')
print(f'Player current airport: {player.airport}')

print(game.closest_airports)