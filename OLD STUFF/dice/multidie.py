import random

min = 1
roll_again = 'y'

while roll_again == 'y':
    max_num = input('How many sides should there be?\n')
    max = int(max_num)
    dice = int(input('How many dice should there be?\n'))
    print('Rolling dice...')
    for i in range(dice):
        diceout = random.randint(min, max)
        print('The Dice Value of Die %d Is: %d\n' % (i + 1, diceout))
    roll_again = input('Would you like to roll again? [y/n] \n')
