import random
import json
from database.db_models import get_questions_avatar_sql

# GET QUESTIONS FOR PLAYER
class Questions:
    def __init__(self):
        self.questions = {}

# SET QUESTIONS IN QUESTIONS INSTANCE
    def set_questions(self, avatar_id):
        questions = get_questions_avatar_sql(avatar_id)
        self.questions = questions

    def return_random_question(self):
        
        questions_dict = {}
        for i, question in enumerate(self.questions):
            questions_dict[f'question-{i+1}'] = f'{question}'

        random_question = random.choice(list(questions_dict.keys()))
        selected_question = questions_dict[f'{random_question}']
        selected_question = selected_question.replace("'", "\"")
        question_dict = json.loads(selected_question)

        return question_dict
    

    def ask_question(self, question):
        print(f'{question["question_text"]}')
        # PUT QUESTIONS IN RANDOM ORDER & PRINT THEM
        
        if question["wrong_answer2"] == '':
            n = random.randint(0, 100)

            if n < 50:
                print(f'''
                    CASE 1
                1. {question["answer"]}
                2. {question["wrong_answer"]}   
                ''')
                return True
            else:
                print(f'''
                    CASE 2
                1. {question["wrong_answer"]}
                2. {question["answer"]}
                ''')
                return False



        # keys = list(question.keys())
        # random.shuffle(keys)
        # shuffled_dict = {key: question[key] for key in keys}

        # print(f'''
        #       ---------------------------------------
        #       {shuffled_dict}
        #       ---------------------------------------
        #       '''
        #       )

        # input_answer = input(int(''))

        # while True:
        #     try:
        #         input_answer = int(input("Enter your choice (1 or 2): "))
        #         if input_answer in [1, 2]:
        #             break  # Valid input, exit the loop
        #         else:
        #             print("Invalid choice. Please enter 1 or 2.")
        #     except ValueError:
        #         print("Invalid input. Please enter a number (1 or 2).")

        # # Now, input_answer contains a valid integer choice (1 or 2)
        # return input_answer


    