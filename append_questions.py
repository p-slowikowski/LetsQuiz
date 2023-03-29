"""Class ApeendQuestion which user can add new question to data"""
import json
from string import ascii_lowercase
from question import Question


class AppendQuestions:
    """ Main class to add a new question to question.json file"""
    def __init__(self, file):
        self.file = file

    def initialize(self):
        """
        Function initialize add new question to data
        return: Noone
        """
        with open(self.file, mode='r', encoding='utf-8') as file:
            feeds = json.load(file)
        id_quest = feeds['questions'][-1]["id"] + 1
        text_question = input("Podaj treść pytania: ")
        lenght_question = int(input("Ile potęcjalnych odpowiedzi będzie miała twoja odpowiedz? "))
        list_answers = []
        for answer, letter in zip(range(lenght_question), ascii_lowercase):
            answer = input(f"Podaj odpowiedz {letter}: ")
            list_answers.append(answer)
        right_answer = input("Która z tych odpowiedzi była poprawna? Wpisz: a/b/c/d? ")
        question = Question(id_quest, text_question, list_answers, right_answer)
        feeds["questions"].append(question.question_to_dict())

        with open(self.file, mode='w', encoding='utf-8') as file:
            json.dump(feeds, file, indent=4, ensure_ascii=False)
