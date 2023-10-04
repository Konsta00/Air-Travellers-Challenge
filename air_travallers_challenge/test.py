from game import Game, Player, Questions
from game.store import Store
import random

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

def setup_game():
    game = Game()
    input_name = input("Enter your name: ")
    game.display_avatars()
    input_avatar = int(input("Select an avatar (1, 2, or 3): "))
    
    player = Player(input_name, input_avatar)
    player.set_starting_airport(player.avatar_id)
    
    game.set_player(player)
    game.set_current_airport()
    game.load_closest_airports()
    
    questions = Questions()
    questions.set_questions(player.avatar_id)

    store = Store()

    return game, player, questions, store

def display_options():
    print("\n╔══════════════════════════╗\n  Air Travellers Challenge\n╚══════════════════════════╝\n")
    print('''
[OPTIONS]
5. Display a clue ($TBD)
6. Use a powerup 
    ''')
def main():
    game, player, questions, store = setup_game()
    
    # PRINT THE QUESTIONS, RANDOMIZE ORDER OF THE QUESTIONS AND
    # RETURN THE RIGHT VALUE THAT MATCHES THE CORRECT ANSWERS INPUT 
    def ask_question():
        question = questions.return_random_question()
        question_bool = questions.ask_question(question)

        input_answer = int(input('Select correct answer by typing the corresponding number: '))

        if input_answer:
            if input_answer == 6:
                print('Which powerup do you want to use: ')
                print(player.powerups)

                # IMPLEMENT USER POWER WHICH SHOW PLAYER POWERS UPS THEY CAN USE IN QUESTION PART OF THE GAME
                player.use_question_powerup('skip_question')

            elif question_bool == input_answer:
                print("\n╔══════════════════════════╗\n  Air Travellers Challenge\n╚══════════════════════════╝\n")

                print('''
                    [CORRECT ANSWER] \n 
100 points added for player.
$100 dollars added to player\'s wallet.''')
                player.update_points(100)
                player.update_budget(25)

                random_bool = random.randint(0, 250)
                if random_bool < 25:
                    player.random_powerup()
                    pass

    ask_question()

    def co2_result():
        pass
    def continuation():
        # CHECK THAT POINTS & BUDGET DONT GO UNDER 0. SET THEM TO 0 IF THEY DO
        player.check_values(game)
        # DISPLAY OPTIONS FOR PLAYER TO CHOOSE FROM
        game.display_options()

        input_continue = int(input('Select (1, 2, 3 or 4): '))
        try:
            if input_continue:
                if input_continue == 1:
                    ask_question()
                elif input_continue == 2:
                    game.print_available_airports()
                    game.travel()
                    game.update_game()
                elif input_continue == 3:
                    store.display_store_options()
                    category_choice = int(input('\n Choose a category (1. Power ups or 2. Plant trees): '))

                    try:
                        if category_choice in [1, 2]:
                            if category_choice == 1:
                                store.purchase_item(player, 'power_ups', category_choice)
                            elif category_choice == 2:
                                store.purchase_item(player, 'plant_trees', category_choice)
                    except ValueError:
                        print('Invalid input')

                    print(player.powerups)

                    # store.purchase_item(player, category_choice)
                elif input_continue == 4:
                    player.display_stats()
        except ValueError:
                print('Invalid input. Please enter a valid selection.')

    while game.game_over is not True:
        continuation()



if __name__ == "__main__":
    main()
    # LASKEA PALJON LENTOKENTTIEN VÄLINEN MATKUSTAMINEN KULUTTAA CO2/KILSA







