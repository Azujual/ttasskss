"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

def isPrime(a):
    res = []
    for i in range(2,99):
        if a % i == 0:
            res.append(i)
    print res
    if len(res) > 1:
        return "Is not a Prime!"
    else:
        return "Is a Prime!"

def listOfPrimes():
    res = []
    listt = []
    for i in range(2,99):
        res = []
        for j in range(2,99):
            if i % j == 0:
                res.append(j)
        if len(res) == 1:
            listt.append(i)
    print listt

listOfPrimes()

while True:
    uinput = raw_input("Please enter any number: ")
    numbr = int(uinput)

    print isPrime(numbr)
    answer = str(uinput)
    if answer.lower() == 'no':
        break

