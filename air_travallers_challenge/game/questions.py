import random
from database.db_models import get_questions_avatar_sql

# GET QUESTIONS FOR PLAYER
class Questions:
    def __init__(self):
        self.questions = {}

    def set_questions(self, avatar_id):
        questions = get_questions_avatar_sql(avatar_id)
        
        self.questions = questions

