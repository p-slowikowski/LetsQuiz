from string import ascii_lowercase


class Question:
    def __init__(self, question_id, question, answers, right_answer):
        self.question_id = question_id
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

    def __str__(self):
        output = "----------------------\n"
        output += f"Pytanie nr.{self.question_id}: {self.question}\n"
        output += "Oto możliwe odpowiedzi...\n"
        for letter, answer in zip(ascii_lowercase, self.answers):
            output += f"Odpowiedz {letter})  {answer}\n"
        return output

    def check_answer(self, user_answer):
        if user_answer == self.right_answer:
            return True

    def question_to_dict(self):
        quest_dict = {}
        quest_dict["id"] = self.question_id
        quest_dict["question"] = self.question
        quest_dict["answers"] = self.answers
        quest_dict["right_answer"] = self.right_answer
        return quest_dict
