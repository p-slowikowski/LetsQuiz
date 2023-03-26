from question import Question


def test_class_question():
    example_class = Question(1, "Test?", ["tak", "nie"], "a")
    example_class2 = Question(1, "Test?", ["tak", "nie"], "a")
    assert type(example_class) == type(example_class2)


def test_check_answer():
    example_class = Question(1, "Test?", ["tak", "nie"], "a")
    function = example_class.check_answer("a")
    assert function


def test__str__():
    example_class = Question(1, "Test?", ["tak", "nie"], "a")
    example_print = "----------------------\n"\
                    "Pytanie nr.1: Test?\n"\
                    "Oto możliwe odpowiedzi...\n"\
                    "Odpowiedz a)  tak\n"\
                    "Odpowiedz b)  nie\n"
    assert str(example_class) == example_print


def test_question_to_dict():
    example_class = Question(1, "Test?", ["tak", "nie"], "a")
    question_to_dict = example_class.question_to_dict()
    example_dict = {"id": 1, "question": "Test?", "answers": ["tak", "nie"], "right_answer": "a"}
    assert example_dict == question_to_dict
