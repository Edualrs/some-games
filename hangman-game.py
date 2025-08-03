'''
😵 Hangman Game

A simple Hangman game developed in Python, played in the terminal. 
The program selects a random word, and the player must guess its 
letters within a limited number of attempts. Great for practicing 
programming logic, string manipulation, and control flow.
'''

import random

vault_of_secrets = ['ABAXAKI', 'LEITE CONDENADO', 'SUCO DE MARAJUCA', 'BERIMBAU']

SECRET_WORD = random.choice(vault_of_secrets)

hidden_secret_word = []

for letter in SECRET_WORD:
    hidden_secret_word.append('_') if letter != ' ' else hidden_secret_word.append(letter)

error_counter = 10
attempted_letters = []

print("welcome to the hangman game (don't make too many mistakes 😵) \n")

while error_counter > 0:
    attempt = input('Your attempt: ').upper()
    situation = ''

    if attempt not in attempted_letters:
        attempted_letters.append(attempt)

        if attempt in SECRET_WORD:

            for position in range(len(SECRET_WORD)):
                if SECRET_WORD[position] == attempt:
                    hidden_secret_word[position] = attempt

        else:
            print('Wrong attempt!')
    else:
        print('This letter has already been tried, try another one!')
    

    for character in hidden_secret_word:
        situation += character

    print(hidden_secret_word, attempted_letters)
    error_counter -= 1






















# while True:

#     guess = input('Guess: ')
#     situation = ''

#     if guess not in attempted_lyrics:
#         attempted_lyrics.append(guess)

#         if guess in SECRET_WORD:

#             for position in range(number_of_letters):
#                 if SECRET_WORD[position] == guess:
#                     hidden_secret_word[position] = guess



#     for character in hidden_secret_word:
#         situation += character


