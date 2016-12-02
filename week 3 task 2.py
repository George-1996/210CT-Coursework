def checknumber(number,smaller=2):
    if smaller>=number:  #base case
        return True
    else:          #recursion
        if number%smaller==0:
            return False
        else:
            return checknumber(number,smaller+1)

print(checknumber(7))


#CHECKNUMBER(number,smaller<-2)
#    if smaller >= number
#        return TRUE
#    else
#        if number % smaller = 0
#            return FALSE
#        else
#            return CHECKNUMBER(number,smaller+1)

