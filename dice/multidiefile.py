import sys
import random

min = 1
roll_again = 'y'

while roll_again == 'y':
    max = int(sys.argv[0])    # How many sides should there be?
    dice = int(sys.argv[1])   # How many dice should there be?
    print('Rolling dice...')
    for i in range(dice):
        diceout = random.randint(min, max)
        print('The Dice Value of Die %d Is: %d\n' % (i + 1, diceout))
    roll_again = sys.argv[2]
