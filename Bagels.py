import random

""" Бублики, короткая игра, где нужно угадать число по подсказкам """
NUM_GIGITS = 3 #длина загаданного числа. 
MAX_GUESSES = 5 #число попыток


def main():
    print(
        """Бублики, дедуктивная логическая игра. 
        Я имею в виду {}-значное число без повторяющихся цифр.
        Попробуйте угадать, что это такое. 
        
        Вот несколько подсказок:
        Когда я говорю: 
        
        Это значит: Пико- Одна цифра правильная, но в неправильном положении.
        Ферми-Одна цифра правильная и находится в правильном положении.
        Бублики-Ни одна цифра не верна.
        
        Например, если секретное число было 248, а вы угадали 843. 
        Ключом к разгадке будет Ферми Пико.""".format(
            NUM_GIGITS
        )
    )


    while True:  # Основной цикл игры.
        # Секретное число
        secretNum = getSecretNum()
        print("Я придумал число.")
        print("У вас есть {} догадок, чтобы попробывать отгодать.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_GIGITS or not guess.isdecimal():
                print("Guess {}:".format(numGuesses))
                guess = input(">")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("У вас закончились догадки.")
                print("Загаданное число было:{}.".format(secretNum))

        print("Хотите сыграть еще раз?(да,нет)")
        if not input("> ").lower().startswith("д"):
            break
    print("Спасибо за игру")


def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр"""
    numbers = list("0123456789")
    random.shuffle(numbers)
    secretNum = ""
    for i in range(NUM_GIGITS):
        secretNum += str(numbers[i])

        return secretNum


def getClues(guess, secretNum):
    """возвращает строку с подсказками"""
    if guess == secretNum:
        return "Ты отгадал!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте.
            clues.append("Ферми")

        elif guess[i] in secretNum:
            # Правильная цифра на неправильном месте.
            clues.append("Пико")
        if len(clues) == 0:
            return "Бублики"
        else:
            # Сортируем подсказки в алфавитном порядке, чтобы их исходный порядок ничего не выдавал.
            clues.sort()
            # Склеиваем подсказки в одну строку
            return " ".join(clues)


if __name__ == "__main__":
    main()
