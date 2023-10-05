from game import Game, Player, Questions
from game.store import Store
import random
from colors import *

print(f'''{color_red}
   _____  .__         ___________                         .__  .__              /\\       
  /  _  \\ |__|______  \\__    ___/___________ ___  __ ____ |  | |  |   __________)/ ______
 /  /_\\  \\|  \\_  __ \\   |    |  \\_  __ \\__  \\\\  \\/ // __ \\|  | |  | _/ __ \\_  __ \\/  ___/
/    |    \\  ||  | \\/   |    |   |  | \\// __ \\ \\   /\\  ___/|  |_|  |_\\  ___/|  | \\/\\___ \\ 
\\____|__  /__||__|      |____|   |__|  (____  /\\_/  \\___  >____/____/\\___  >__|  /____  >
        \\/                                  \\/          \\/               \\/           \\/ 
              _________ .__           .__  .__                                           
              \\_   ___ \\|  |__ _____  |  | |  |   ____   ____    ____   ____             
              /    \\  \\/|  |  \\\\__  \\ |  | |  | _/ __ \\ /    \\  / ___\\_/ __ \\            
              \\     \\___|   Y  \\/ __ \\|  |_|  |_\\  ___/|   |  \\/ /_/  >  ___/            
               \\______  /___|  (____  /____/____/\\___  >___|  /\\___  / \\___  >           
                      \\/     \\/     \\/               \\/     \\//_____/      \\/            
{color_end}''')

print(f'''{color_bright_magenta}
╭──────────────────────────────────────────────────────────────────────╮
│                              Game Rules                              │
╰──────────────────────────────────────────────────────────────────────╯

In this game, your mission is to travel between airports and accumulate points while minimizing your carbon emissions. 

Your journey begins at your chosen starting airport, depending on your avatar:
-  Donald Trump plays in the United States.
-  Mona Lisa plays in France.
-  Felipe IV plays in Spain.

The difficulty level is also determined by your avatar:
-  Donald Trump represents the easiest level.
-  Mona Lisa provides a medium challenge.
-  Felipe IV offers the hardest experience.

Your objective is to reach 1000 points by answering questions and keeping your CO2 emissions as low as possible.
As you are playing you earn point and money by answering correctly. Wrong answers deducts your points.

You have the power to make a positive impact by planting trees to reduce your emissions. 
Additionally, there are power-ups available for purchase to help you skip questions and avoid losing points.
{color_end}
''')
def setup_game():
    game = Game()
    input_name = input("Enter your name: ")
    player = None
    while player is None:
        try:
            game.display_avatars()
            input_avatar = int(input("Select an avatar 1-3: "))
            if input_avatar in [1, 2, 3]:
                player = Player(input_name, input_avatar)
                player.set_starting_airport(player.avatar_id)
            else:
                print(f'{color_bright_red}Invalid avatar. Select from 1-3.{color_end}')
        except ValueError:
            print(f'{color_bright_red}Invalid input{color_end}')

    game.set_player(player)
    game.set_current_airport()
    game.load_closest_airports()
    
    questions = Questions()
    questions.set_questions(player.avatar_id)

    store = Store()

    return game, player, questions, store

def main():
    game, player, questions, store = setup_game()
    
    # PRINT THE QUESTIONS, RANDOMIZE ORDER OF THE QUESTIONS AND
    # RETURN THE RIGHT VALUE THAT MATCHES THE CORRECT ANSWERS INPUT 
    def ask_question():
        input_ = None
        while input_ is None:  
            try: 
                question = questions.return_random_question()
                question_bool = questions.ask_question(question)

                input_answer = int(input('Select correct answer by typing the corresponding number: '))
                if input_answer in [1,2,3,6]:
                    input_ = True
                    if input_answer == 6:
                        # IMPLEMENT USER POWER WHICH SHOW PLAYER POWERS UPS THEY CAN USE IN QUESTION PART OF THE GAME
                        bool = player.use_question_powerup()

                        if bool == True:
                            game.print_available_airports()
                            game.travel()

                    elif question_bool == input_answer:
                        print('''
                    ╔══════════════════════════╗ 
                      Air Travellers Challenge
                    ╚══════════════════════════╝''')

                        print(f'''
                        {color_bright_green}
                [CORRECT ANSWER] \n 
                100 points added to player.
                $75 dollars added to player\'s wallet.
                        {color_end}
                    ''')
                        player.update_points(100)
                        player.update_budget(75)
                        player.update_questions()

                        random_bool = random.randint(0, 250)
                        if random_bool < 40:
                            player.random_powerup()

                    elif question_bool != input_answer:
                        print('''
                    ╔══════════════════════════╗ 
                      Air Travellers Challenge
                    ╚══════════════════════════╝''')
                        print(f'''
                        {color_bright_red}
                [INCORRECT ANSWER] \n 
                Points deducted by 65.
                        {color_end}''')
                        player.update_points(-65)
                        player.current_answered += 1
            except ValueError:
                print(f'{color_bright_red}Invalid input{color_end}')

    def game_loop():
        # CHECK THAT POINTS & BUDGET DONT GO UNDER 0. SET THEM TO 0 IF THEY DO
        player.check_values(game)
 
        if player.current_answered > 2:
            game.display_options()
            input_continue = int(input('                Select 1-3: '))

            try:
                if input_continue:
                    if input_continue == 1:
                        game.print_available_airports()
                        game.travel()
                        game.update_game()
                    elif input_continue == 2:
                        player.display_powerups() 
                    elif input_continue == 3:
                        store.display_store_options()
                        store.buy()
            except ValueError:
                    print(f'{color_bright_red}Invalid input. Please enter a valid selection.f{color_bright_red}')
        else:
            if player.current_answered == 0:
                ask_question()
            
            game.display_options()
            # ASK USER TO SELECT BETWEEN THE OPTIONS 
            input_continue = int(input('                Select 1-4: '))
            try:
                if input_continue:
                    if input_continue == 1:
                        ask_question()
                    elif input_continue == 2:
                        game.print_available_airports()
                        game.travel()
                        game.update_game()
                    elif input_continue == 3:
                        player.display_powerups()       
                    else:
                        store.display_store_options()
                        store.buy(player)
            except ValueError:
                    print(f'{color_bright_red}Invalid input. Please enter a valid selection.{color_end}')
            
    while game.game_over is not True:
        game_loop()

if __name__ == "__main__":
    main()


# TODO: POWERUP OSTO JA KÄYTTÖ ERI PELIN TILANTEISSA





