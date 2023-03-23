"""From this file are realise the main functions Quiz app"""
import json
from question import Question
from append_questions import AppendQuestions


class Game:
    """
    The Main Class stores all functions
    """
    def __init__(self, file):
        self.file = file
        self.score = 0

    def initialize_game(self):
        """
        Initalize the main funkcjon app.
        :rtype: object class Game
        """
        with open(self.file, mode='r', encoding='utf-8') as file:
            feeds = json.load(file)
        game = input("Czy jesteś gotowy do gry? tak/nie ")
        name = input("Zanim zaczniemy, podaj swoje imię: ")
        if game == "tak":
            print("Więc zaczynamy zabawę")
            for key in feeds["questions"]:
                question = Question(key['id'], key['question'], key["answers"], key['right_answer'])
                print(question)
                user_answer = input("Podaj właściwą odpowiedz...")
                if question.check_answer(user_answer) is True:
                    self.score += 1
            print(f"Brawo {name} zdobywasz {self.score} punktów!")

        with open("users_score.json", "r") as file:
            results = json.load(file)

        results["dict_scores"].append({
            "name": name,
            "points": self.score
        })

        with open("users_score.json", "w") as file:
            json.dump(results, file, indent=4)

    def initialize_append_question(self):
        """
        Function which append new question to data (json)
        :rtype: object
        """
        x = input("Czy chcesz dodać pytanie?")
        if x == "tak":
            append = AppendQuestions(self.file)
            a = append.initialize()
            print(a)

    def initialize_list_score(self):
        """
        function show TOP 10 the highest scores users
        :rtype: object
        """
        with open("users_score.json", "r") as file:
            results = json.load(file)
            sort_users = sorted(results["dict_scores"], key=lambda d: d["points"], reverse=True)
        print("Hall of Fame!!!")
        print("TOP 10")
        for user in range(9):
            print(f"Miejsce nr.{user+1}: {sort_users[user]['name']}. Ilość punktów: {sort_users[user]['points']}")

    def questions_list(self):
        """
        Function show all questions with possible answers.
        :rtype: object
        """
        with open(self.file, mode='r', encoding='utf-8') as file:
            feeds = json.load(file)
        for key in feeds["questions"]:
            question = Question(key['id'], key['question'], key["answers"], key['right_answer'])
            print(question)








