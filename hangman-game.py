SECRET_WORD = 'abaxaki'

correct_letter = []

number_of_letters = len(SECRET_WORD)
hidden_secret_word = '_' * number_of_letters

attempts = 15

hidden_secret_word = list(hidden_secret_word)
while True:
    guess = input('Guess: ')

    if guess in SECRET_WORD:
        correct_letter.append(guess)
    else:
        print('Try again!')

    print(hidden_secret_word, correct_letter)

    attempts -= 1

    if attempts == 0:
        break