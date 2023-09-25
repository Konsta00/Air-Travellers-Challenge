# IMPORT GAME 6 PLAYER CLASS + NEEDED MODULES
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

# SELECT NAME FOR PLAYER
input_name = str(input('Select a name for player: '))

# CREATE GAME INSTANCE
game = Game()

#PRINT AVATARS FOR USER TO SELECT
game.print_avatars()

input_avatar = int(input())

# CRETE NEW PLAYER INSTANCE WITH GIVEN NAME AND GIVEN AVATAR
player = Player(input_name, input_avatar)


# SET PLAYER AS PLAYER INSTANCE IN GAME INSTANCE
game.set_player(player)

# SET PLAYER INSTANCE STARTING AIPORT BASED ON AVATAR & SET GAME INSTANCED CURRENT AIRPORT
player.set_starting_airport(player.avatar_id)
game.set_current_airport()
 

# SET CLOSEST AIRPORTS TO GAME

game.set_closest_airports()
print(f'Game closest airport: {game.closest_airports}')


# CREATE NEW PLAYER IN DATABASE
player.insert_player_to_database()

# GET QUESTIONS FOR PLAYER

# DEBUG & DEVELOPEMENT

print(f'Player name: {player.name}')
print(f'Player character: {player.avatar_id}')
print(f'Player current airport: {player.airport}')

# print(game.closest_airports)