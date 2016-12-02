def hps(number):                          
    for i in range(2,int(number)):
        if i*i > int(number):
            return i - 1
        


print(hps(38))

#HPS(number)
#    for i<-1 to length(2,number)
#        if i mult i > number
#            return i - 1
