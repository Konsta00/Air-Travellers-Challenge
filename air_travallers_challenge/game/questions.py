import random
from database.db_models import get_questions_avatar_sql

# GET QUESTIONS FOR PLAYER
def get_questions_avatar(avatar_id):
    questions = get_questions_avatar_sql(avatar_id)

    print(questions)


    