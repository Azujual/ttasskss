"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence"""

fib = [1, 1, 2, 3, 5, 8, 13]

def uInput():
    inp = raw_input("Please enter number of Fibonnaci elements you want me to generate: ")
    return int(inp)

def genFib(gg):
    i = 1
    if gg > 1:
        listFib = [1,1]
        while i < (gg - 1):
            listFib.append(listFib[i] + listFib[i - 1])
            i += 1
        return listFib
    elif gg == 1:
        listFib = [1]
        return listFib
    else:
        listFib = []
        return listFib

a = uInput()
print genFib(a)

