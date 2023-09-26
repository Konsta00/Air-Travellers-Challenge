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


    def print_question(self, question):
        print(f'''
            {question["question_text"]}

1. {question["answer"]}
2. {question["wrong_answer"]}
3. {question["wrong_answer2"]}    
        ''')
        
# {'avatar_id': 1, 
# 'question_text': 'Mik„ on luokka (class) Python-ohjelmoinnissa?', 
# 'clue1': 'Se on objekti, joka voi sis„lt„„ toiminnallisuutta', 
# 'clue2': 'Se on Pythonin avainsana', 
# 'answer': 'Luokka on objekti, joka voi sis„lt„„ toiminnallisuutta', 
# 'wrong_answer': 'Se on funktio', 
# 'wrong_answer2': ''}