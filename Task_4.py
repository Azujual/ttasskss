"""Create a program that asks the user for a number
and then prints out a list of all the divisors of that number.
"""

num = int(input("Please choose a number to divide: "))

divisorList = []

for number in range(1,num+1):
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
