import random
a = [random.randrange(0, 50, 1) for i in range(0, 51, 1)] # duplicates are possible
b = [random.randrange(0, 50, 1) for i in range(0, 51, 1)]# duplicates are possible

c = random.sample(range(100), 15) # .sampler returns list of unique items of sequence.
print "C: \n%s" %c
d = random.sample(range(50), 15) # .sampler returns list of unique items of sequence.
print "D: \n%s" %d

"""

This program returns a unique list that contains only the elements

that are common between the list a and b (without duplicates).

"""

def list_overlap(a, b):
    new_lst = []
    for item in b:
        if item in a and item not in new_lst:
            new_lst.append(item)
    return new_lst

print list_overlap(c, d)
