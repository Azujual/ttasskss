import sys
import datetime

name = raw_input("Enter your name: ")
age = raw_input("How old are you: ")
repeats = raw_input("How many times you want me to print message: ")

now = datetime.datetime.now()
y = now.year

hundred = int(y) + (100 - int(age))
print hundred

print "Hello, %s In year %d you will turn 100 years\n" %(name, hundred) * int(repeats)


