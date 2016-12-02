def binarySearch(alist, low,high):
    first = 0
    last = len(alist)-1
    found = False
	
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] >=low and alist[midpoint] <= high:
            found = True
        else:
            if high < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
	
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3,11))
print(binarySearch(testlist, 33,40))

#BINARYSEARCH(alist, low, high)
#    first <- 0
#    last <- length(alist) - 1
#    found <- FALSE
#    while first <= last and not found:
#        midpoint <- (first + last) // 2
#        if alist[midpoint] >= low and alist[midpoint] <= high
#            found <- TRUE
#        else
#            if high < alist[midpoint]
#               last <- midpoint - 1
#            else
#                first <- midpoint + 1
#    return found


#################################################################
#Title - The Binary Search
#Author - Brad Miller, David Ranum
#Date - 2014
#Code version - 
#Available - https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
#################################################################
