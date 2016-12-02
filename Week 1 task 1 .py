#ask = list(input("Enter list of integers"))/wasnt sure if we have to have an user input
import random
ask=[1,2,3,4,5,6,7,8,9]
empty = []
#print (len(ask))
while len(ask) > 0:
    rnd=random.randint(0,len(ask)-1)
    empty.append(ask[rnd])
    ask.pop(rnd)
print(empty)

#BigO(n)
