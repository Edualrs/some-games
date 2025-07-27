# Configuring players
X = 'X'
O = 'O'
player_turn = X

# Setting up the board
positions = [1,2,3,4,5,6,7,8,9]
board = '''
{}|{}|{}
{}|{}|{}
{}|{}|{}
'''

print(f'''
👵 Welcome to the COOLEST Text Tic Tac Toe Game!

This is our board, Let's start the game ...
{board.format(*positions)}''')

positions = [' ',' ',' ',' ',' ',' ',' ',' ',' '] # Resetting the board

while True:

    # information about whose turn it is, and a ternary operation that changes the letters to more pleasant-to-see emojis
    print(f"It's {'✖️ ' if player_turn == 'X' else '⭕'} turn to play") 
    try: 
        play = int(input('Choose a square: '))
        real_play = play - 1

        if positions[real_play] == X or positions[real_play] == O:
            print('⚠️ Square already chosen. Try another one! \n')
            continue
        else:
            positions[real_play] = player_turn

    except IndexError:
        print('⚠️ Invalid play. Try a square within the possible ones! \n')
        continue
    except ValueError:
        print('⚠️ Invalid play. Please enter only the square number! \n')
        continue

    print(board.format(*positions)) # Showing current board status

    # Evaluating squares horizontally
    if (player_turn == positions[0] and player_turn == positions[1] and player_turn == positions[2]) or \
        (player_turn == positions[4] and player_turn == positions[5] and player_turn == positions[6]) or \
        (player_turn == positions[7] and player_turn == positions[8] and player_turn == positions[9]):
        print(f'{'✖️ ' if player_turn == 'X' else '⭕'} Win! 🎉')
        break

    # Evaluating squares vertically
    elif (player_turn == positions[0] and player_turn == positions[3] and player_turn == positions[6]) or \
        (player_turn == positions[1] and player_turn == positions[4] and player_turn == positions[7]) or \
        (player_turn == positions[2] and player_turn == positions[5] and player_turn == positions[8]):
        print(f'{'✖️ ' if player_turn == 'X' else '⭕'} Win! 🎉')
        break

    # Evaluating squares on the diagonal
    elif (player_turn == positions[0] and player_turn == positions[4] and player_turn == positions[8]) or \
        (player_turn == positions[2] and player_turn == positions[4] and player_turn == positions[6]):
        print(f'{'✖️ ' if player_turn == 'X' else '⭕'} Win! 🎉')
        break

    # Evaluating draw
    elif ' ' not in positions:
        print('👵 The game is a DRAW.')

    # Changing player
    if player_turn == 'X':
        player_turn = 'O'
    else:
        player_turn = 'X'