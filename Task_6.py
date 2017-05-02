"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

inp = raw_input("Please enter polindrom: ")

polindroms = []
polindroms.append(inp)

for i in polindroms:
    check = -1
    for j in range(len(i) / 2):
        #print "working with " + i
        #print i[j] + " making decision " + i[-1 + 0 - j]
        if i[j] != i[-1 + 0 - j]:
            print i + " is not polindorme"
            check = 0
            break
        else:
            check = 1
    if check == 1:
        print i + " is polindrome"
