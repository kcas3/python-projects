import random
minval = 1
maxval = 6

roll_again = "yes"

while roll_again == "yes" or "y":
    print "Rolling dice..."
    print "Dice value is" + random.randint(min, max)

if __name__ == '__main__':
    main()
