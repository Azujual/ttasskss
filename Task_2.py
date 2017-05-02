"""Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num)
and one number to divide by (check).
If check divides evenly into num,
tell that to the user.
If not, print a different appropriate message."""

number = int(input("Please enter any integer number: "))
divider = int(input("Please enter additional number"))

if number % 2 == 0:
    print "Number you entered is even"
    if number % 4 == 0:
        print "And your number also is multiple of 4"
else:
    print "Number you entered is odd"

if number % divider == 0:
    print "%d is multiple of %d" % (number, divider)

