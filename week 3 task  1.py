def swap(n,i):
    value=""
    if i<len(b)-1:
        value=swap(n,i+1)
    return value + " " + n[i]
a = "awesome really is This"
b=a.split(" ")
print(swap(b,0))

#BigO(n)


#SWAP(n,i)
#    value <- " "                                    (empty list)
#    if i < length(b) - 1
#        value <-REC(n, i+1)
#    return value + " " + n[i]
#a<- "awesome really is This"
#b<- a.split(" ")
#print swap(b,0)

#BigO(n)
