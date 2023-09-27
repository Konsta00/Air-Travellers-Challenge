# IMPORT GAME 6 PLAYER CLASS + NEEDED MODULES
from game import Game, Player, Questions

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
    
    return game, player, questions

def display_options():
    print('''
[OPTIONS]
5. Display a clue ($TBD)
6. Use a powerup 
    ''')
def main():
    game, player, questions = setup_game()
    
    question = questions.return_random_question()
    
    game.display_avatars()
    display_options()
    
    # PRINT THE QUESTIONS, RANDOMIZE ORDER OF THE QUESTIONS AND
    # RETURN THE RIGHT VALUE THAT MATCHES THE CORRECT ANSWERS INPUT 
    question_bool = questions.ask_question(question)
    
    input_answer = int(input('Select correct answer by typing the corresponding number: '))
    
    if input_answer:
        if question_bool == input_answer:
            print('''
                  [CORRECT ANSWER] \n 
100 points added for player.
$100 dollars added to player\'s wallet.''')
            player.update_points(100)
            player.update_budget(100)
    
    # CHECK THAT POINTS & BUDGET DONT GO UNDER 0. SET THEM TO 0 IF THEY DO
    player.check_values()        
    
    # DISPLAY OPTIONS FOR PLAYER TO CHOOSE FROM
    game.display_options()

    input_continue = int(input('Select (1, 2, 3 or 4)'))
    try: 
        if input_continue:
            if input_continue == 1:
                pass
            elif input_continue == 2:
                game.print_available_airports()
                game.travel()
            elif input_continue == 3:
                pass
            elif input_continue == 4:
                pass
    except ValueError:
            print('Invalid input. Please enter a valid selection.')


# TODO: CHEECK WHAT THE USER CHOOSES FROM INPUT.
# TODO:
    

    print('NEW VALUES: \n')
    player.print_player()



if __name__ == "__main__":
    main()











