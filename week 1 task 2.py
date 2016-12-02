def factorial(number):
    if number <=1:      
        return 1
    if number >=1:
        fact = number * factorial(number-1)   ####recursively finding thefactorial of a number
        return fact

def counting(number):
    fact = int(factorial(number))
    a = str(fact)
    b = []        #### create and empty list and adds the numbers of the factorials seperately by using a for loop
    for i in a:
        b.append(int(i))
        c = b.count(int(0)) 
    return c


print(counting(12))

#BigO(n)
