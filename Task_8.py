"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
Discussion"""

import random

a = 1
pc_choice = ['rock', 'paper', 'scissors']

while a == 1:
    player_choice = raw_input("Make your choice: ")
    palyer_choice = str(player_choice)
    if player_choice.lower() not in pc_choice:
        print "Please try again"
        continue
    print "Player's choice: " + player_choice.lower()
    pc_rand = random.randint(0,2)
    print pc_rand
    print "PC's choice: " + pc_choice[pc_rand]
    if player_choice.lower() == pc_choice[0] and pc_choice[pc_rand] == pc_choice[2]:
        print 'Player wins!'
        a = 0
    elif player_choice.lower() == pc_choice[1] and pc_choice[pc_rand] == pc_choice[0]:
        print 'Player wins!'
        a = 0
    elif player_choice.lower() == pc_choice[2] and pc_choice[pc_rand] == pc_choice[1]:
        print 'Player wins!'
        a = 0
    elif player_choice.lower() == pc_choice[0] and pc_choice[pc_rand] == pc_choice[1]:
        print 'PC wins!'
        a = 0
    elif player_choice.lower() == pc_choice[1] and pc_choice[pc_rand] == pc_choice[2]:
        print 'PC wins!'
        a = 0
    elif player_choice.lower() == pc_choice[2] and pc_choice[pc_rand] == pc_choice[0]:
        print 'PC wins!'
        a = 0
    else:
        print "Draw!!!"
