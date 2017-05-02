




def isPrime(num):
    a = [x for x in range(2,num - 1) if num % x == 0]
    if len(a) > 0:
        print "%d is not Prime!" % (num)
    else:
        print "%d is Prime!" % (num)
    print a

while 1:
    num = raw_input("Give me a number (or 'NO' for exit): ")
    if num.lower() == 'no':
        break
    else:
        isPrime(int(num))
