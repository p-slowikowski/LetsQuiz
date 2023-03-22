from question import Question


def test_class_question():
    example_class = Question(1, "Test?", ["tak", "nie"], "a")
    example_class2 = Question(1, "Test?", ["tak", "nie"], "a")
    assert type(example_class) == type(example_class2)


def test_check_answer():
    example_class = Question(1, "Test?", ["tak", "nie"], "a")
    function = example_class.check_answer("a")
    assert function
