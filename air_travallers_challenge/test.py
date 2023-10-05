from game import Game, Player, Questions
from game.store import Store
import random

print('\033[91m' + '''
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
\033[0m''')

print('\033[92m' + '''
╭──────────────────────────────────────────────────────────────────────╮
│                              Game Rules                               │
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

You have the power to make a positive impact by planting trees to reduce your emissions. 
Additionally, there are power-ups available for purchase to help you skip questions and avoid losing points.

''' + '\033[0m')
print('''
        Rules of the game. In this game you need to travel between airports. Your starting airport is determined by you avatar. 
        Donald Trump plays in the United States. Mona Lisa plays in France and Felipe IV in Spain. Difficulty level is also determined by your avatar.
        Donald Trump is easiest and Felipe IV is the hardest.
        Your goal is to get 1000 points by answering questions and create as little CO2 emissions as possible.
        You can also plant trees to lower your emissions in the store. There are also power ups that you can buy to, for example skip questions to avoid losing points.
      ''')

def setup_game():
    game = Game()
    input_name = input("Enter your name: ")
    player = None
    while player is None:
        try:
            game.display_avatars()
            input_avatar = int(input("Select an avatar (1, 2, or 3): "))
            if input_avatar in [1, 2, 3]:
                player = Player(input_name, input_avatar)
                player.set_starting_airport(player.avatar_id)
            else:
                print("Invalid avatar.")
        except ValueError:
            pass

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
                print('''
                ╔══════════════════════════╗ 
                  Air Travellers Challenge
                ╚══════════════════════════╝
                      ''')

                print('\033[92m'+'''
                    [CORRECT ANSWER!] \n 
            100 points added for player.
            $75 dollars added to player\'s wallet.
            '''+'\033[0m')
                player.update_points(100)
                player.update_budget(75)
                player.update_questions()

                random_bool = random.randint(0, 250)
                if random_bool < 40:
                    player.random_powerup()

            elif question_bool != input_answer:
                print("\n╔══════════════════════════╗\n  Air Travellers Challenge\n╚══════════════════════════╝\n")
                print('''
                     [WRONG ANSWER!] \n 
                Points will be deducted by 65.'''+'\033[0m')
                player.update_points(-65)
                player.current_answered += 1

    def game_loop():
        # CHECK THAT POINTS & BUDGET DONT GO UNDER 0. SET THEM TO 0 IF THEY DO
        player.check_values(game)

        print('''
                ╔══════════════════════════╗ 
                  Air Travellers Challenge
                ╚══════════════════════════╝
                      ''')

        if player.current_answered > 2:
            game.display_options()
            input_continue = int(input('Select (1 or 2): '))
            try:
                if input_continue:
                    if input_continue == 1:
                        game.print_available_airports()
                        game.travel()
                        game.update_game()
                    elif input_continue == 2:
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
            except ValueError:
                    print('Invalid input. Please enter a valid selection.')
        else:
            if player.current_answered == 0:
                ask_question()
            
            game.display_options()
            input_continue = int(input('Select (1, 2 or 3): '))
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
            except ValueError:
                    print('Invalid input. Please enter a valid selection.')
            
    while game.game_over is not True:
        game_loop()

if __name__ == "__main__":
    main()

# TODO: PELIN ALKUUN SÄÄNNÖT/TARINA.
# TODO: POWERUP OSTO JA KÄYTTÖ ERI PELIN TILANTEISSA
# TODO: NÄKYVIIN LENTTOKENTTIEN ETÄISYYS KUN MATKUSTAA
# TODO: TARKISTA KÄYTTÄJÄN INPUT JOKAISESSA KOHDASSA JOSSA KÄYTTÄJÄLTÄ KYSYTÄÄN SYÖTETTÄ
# TODO: KUN MATKUSTAA NÄYTTÄÄ LENTOKENTÄN JOHON MATKUSTI




