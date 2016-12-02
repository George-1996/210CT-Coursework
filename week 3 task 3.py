def remove(string):
    a = list(string)
    v = ["a","i","o","u","e"]
    for e in v:
        if e in a:
            c = list(i for i in a if i not in v)
            d = "".join(c)      #built in function that converts list to string
            return d
        
print(remove("recursion"))


#REMOVE(string)
#    a <- list(string)
#    v <- ["a","i","o","u","e"]
#    for e in v:
#        if e in a:
#            c <- list(i for i in a if i not in v)
#            d <- "".join(c)
#            return d
#
#print remove("recursion")
