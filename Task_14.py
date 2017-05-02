"""Write a program or function that takes a list
and returns a new list that contains all the elements
of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""


names = ["Michele", "Robin", "Sara", "Michele"]
print names
names = set(names)
names = list(names)
print(names)
