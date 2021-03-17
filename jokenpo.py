import random

def play():
    user = input("What's your choice? \n 'r' for rock, \n 'p' for paper, \n 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It was a tie'

    if wins(user, computer):
        return 'You won!'

    return 'You lost!'

def wins(player, opponent):
    if (player == 'r' and opponent == 's') \
       or (player == 'p' and opponent == 's') \
       or (player == 's' and opponent == 'p'):
        return True

print(play())
