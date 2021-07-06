# This is a little Number Guessing Game, hope You'll enjoy it!

import random
import math

print("\nHi, and welcome to the game!\n")

lower_bond = int(input('Please, enter Lower bond: '))
upper_bond = int(input('Please, enter Upper bond: '))

rand_number = random.randint(lower_bond, upper_bond)
nr_of_guesses = math.log(upper_bond-lower_bond+1, 2)

print('\nYou have only', "{:.0f}".format(nr_of_guesses), 'number of guesses!\n')

count = 0
while count < nr_of_guesses:
    count += 1
    user_number = int(input('\nGuess a number: '))
    if user_number < rand_number:
        print('You guessed too','\033[1m' + 'small' + '\033[0m\n', "{:.0f}".format(nr_of_guesses-count), 'tries left')
    elif user_number > rand_number:
        print('You guessed too','\033[1m' + 'high' + '\033[0m\n', "{:.0f}".format(nr_of_guesses-count), 'tries left')
    else:
        print('Congratulations! You did it in', count, 'try!')
        break

if count > nr_of_guesses:
    print('Better luck next time!\nThe number was:', rand_number)



