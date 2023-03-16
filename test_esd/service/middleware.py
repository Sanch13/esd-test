from esd.models import EsdTest
from random import sample


def get_random_questions() -> list:
    """Get ten random questions from DataBase"""
    all_questions = EsdTest.objects.all()
    ten_questions = sample(list(all_questions), 10)
    return ten_questions


user_data = {
    'score': 0,
    'questions': get_random_questions(),
}
