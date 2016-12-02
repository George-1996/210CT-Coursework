def Sequence(array):
    counter = 0
    length = 0
    sequence=[]
    for i in range(len(array)-1):
        counter+=1
        #print  (counter)
        length+=1
        #print (length)
        if(array[i]>array[i+1]):
            if(length>len(sequence)):
                sequence=[]
                for elements in range(counter-length,counter):
                    sequence.append(array[elements])
                #print(sequence)
            length=0

    if(length+1>len(sequence)):
        sequence = array[ counter-length :  ]

    
    return sequence

print(Sequence([1,2,3,4,2,9,18,64,128,69,2,5,9,11,12,13]))


