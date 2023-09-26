import random
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

        return selected_question

        # print(questions_dict)
        # return random.choice(list(questions_dict.keys()))

