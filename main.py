# Введение функции
def hangman(word):
    wrong = 0
    # Список в котором храниться игра
    stages = ["",
              " ____________                     ",
              " |           |                    ",
              " |           |                    ",
              " |           0                    ",
              " |         / | \                  ",
              " |          / \                   ",
              " |                                "
              ]
    # Вводим переменную которая отслеживает каждую букву в загаданном слове
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на казнь")
    # Цикл благодаря которому работает игра
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Введите букву")
        # Замена "_" на букву
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"

        # Выведение висилицы
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        # Код выполняется в случае угадывания слова
        if "_" not in board:
            print("Вы выйграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    # Код выводиться в случае пройгрыша
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Вы проиграли. Было загадано слово: {}".format(word))


hangman("человек")
