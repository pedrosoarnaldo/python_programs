import random
import time

def roll_dice():
    return random.randint(1,6), random.randint(1,6)

print('-' * 40)
print('Welcome to dice game')
print('-' * 40)

name = str(input('Insert your name: '))

while True:
    (player, computer) = roll_dice()

    print('')
    print(f'Your dice {player}')

    print('')
    print("Rolling the computer's dice ... wait a few seconds")
    print('')

    for i in range(3):
        time.sleep(1)

    print(f"Computer's dice {computer}")
    print('')

    if player > computer:
        print(f'Congratulations {name} you have won the game!')
    elif player < computer:
        print(f'Sorry {name} the computer has won the game!')
    else:
        print(f'We had a tie!')

    print('')
    play_again = str(input('Do you wanna play again? (s/n) '))

    if (play_again == 's') or (play_again == 'S'):
        continue
    else:
        break

