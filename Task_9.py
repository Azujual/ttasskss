"""Generate a random number between 1 and 9 including 1 and 9.
Ask the user to guess the number, then tell them whether they guessed too low, too high,
or exactly right.

Extras:
1 2 3 4 5 6 7 8 9
Keep the game going until the user types exit
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

chr = 'true'
count = 0
rguess = 0

while chr:
    count += 1
    guess = int(raw_input("Please enter your guess (1-9): "))
    goal = random.randint(1,9)
    print goal
    if guess == goal:
        print "Bingo!!!"
        rguess += 1
    elif guess < goal:
        print "Your guess is too low"
    else:
        print "Your guess is too hight"
    answer = str(raw_input("Do you want to try again? (YES/NO)"))
    print answer
    if answer.lower() == 'no':
        chr = False
    print chr == answer.lower()

print "From %d tries you guessed %d" %(count, rguess)
