import random
min = 1
max = 6
die = random.randint(min, max)
roll_again = 'yes'

if die == 1:
    out = '     \n  *  \n     '
if die == 2:
    out = '*    \n     \n    *'
if die == 3:
    out = '*    \n  *  \n    *'
if die == 4:
    out = '*   *\n     \n*   *'
if die == 5:
    out = '*   *\n  *  \n*   *'
if die == 6:
    out = '* * *\n     \n* * *'

print('Your Number Is: %d' % die)
print(out)
