
vowels = ["a","i","o","u","e", "A","E","I","O","U"]

def removeVowel(theString, complete=""):
    #print(theString,"/",complete)
    if len(theString)==0:  #base case
        return complete
    else:     #recursive
        keep=""
        if not theString[0] in vowels:
            keep=theString[0]
        
        return removeVowel(theString[1:],complete+keep)

print (removeVowel("Recursion"))

#vowels <- ["a","i","o","u","e","A","E","I","O","U"]
#
#REMOVEVOWEL(theString, complete <- " ")
#    if length(theString)=0
#        return complete
#    else
#        keep <- " "
#        if not theString(0) in vowels
#            keep <-theString(0)
#        return REMOVEVOWEL(theString[1:],complete+keep]
#
#print REMOVEVOWEL("Recursion")
