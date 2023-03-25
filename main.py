from game import Game


def initialize_menu():
    print("Witaj w grze Let's Quiz!")

    while True:
        game = Game("questions.json")
        print("-------------------------------------------")
        print("Obecnie masz do wyboru następujące opcje...")
        print("1. Zagraj w Quiz")
        print("2. Dodaj pytanie do bazy danych")
        print("3. Sprawdz liste wyników")
        print("4. Lista pytań")
        user_choice = int(input("Wpisz odpowiedni numer... "))
        if user_choice == 1:
            game.initialize_game()
        elif user_choice == 2:
            game.initialize_append_question()
        elif user_choice == 3:
            game.initialize_list_score()
        elif user_choice == 4:
            game.questions_list()


initialize_menu()



