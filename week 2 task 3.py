b = [[7,3,5],
     [4,5,9],
     [2,3,1]]

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result_add = [[0,0,0],
              [0,0,0],
              [0,0,0]]

result_sub = [[0,0,0],
              [0,0,0],
              [0,0,0]]

result_multi = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]

result_multi_with_number = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]

def addition(m_one,m_two):
    for x in range(len(m_one)):
        for y in range(len(m_one[0])):
            result_add[x][y] = m_one[x][y] + m_two[x][y]

def subtraction(m_one,m_two):
    for x in range(len(m_one)):
        for y in range(len(m_one[0])):
            result_sub[x][y] = m_one[x][y] - m_two[x][y]

def multiplicationwithnumber(matrix,number):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            result_multi_with_number[x][y] = matrix[x][y] * number

def multiplication(m_one,m_two):
    for x in range(len(m_one)):   #rows of m_one
        for y in range(len(m_two[0])):    #columns of m_two
            for x2 in range(len(m_two)):   #rows of m_two
                result_multi[x][y] = result_multi[x][y] + m_one[x][x2] * m_two[x2][y]


addition(b,a)
multiplicationwithnumber(result_add,2)
multiplication(b,a)
subtraction(result_multi,result_multi_with_number)

for r in result_add:
    print(r)
for r in result_multi_with_number:
    print(r)
for r in result_multi:
    print(r)
for r in result_sub:
    print(r)

##b <- [[7,3,5],[4,5,9],[2,3,1]]
##
##a <- [[1,2,3],[4,5,6],[7,8,9]]
##
##result_add <- [[0,0,0],[0,0,0],[0,0,0]]
##
##result_sub <- [[0,0,0],[0,0,0],[0,0,0]]
##
##result_multi <- [[0,0,0],[0,0,0],[0,0,0]]
##
##result_multi_with_number <- [[0,0,0],[0,0,0],[0,0,0]]
##
##ADDITION(m_one,m_two)
##    for x<-1 to length(m_one)
##        for y<- to length(m_one[1])
##            result_add[x][y] <- m_one[x][y] + m_two[x][y]
##
##SUBTRACTION(m_one,m_two)
##    for x<-1 to length(m_one)
##        for y<-1 to length(m_one[1])
##            result_sub[x][y] <- m_one[x][y] - m_two[x][y]
##
##MULTIPLICATIONWITHNUMBER(matrix,number)
##    for x<-1 to length(matrix)
##        for y<-1 to length(matrix[1])
##            result_multi_with_number[x][y] <- matrix[x][y] * number
##
##MULTIPLICATION(m_one,m_two)
##    for x<- to length(m_one) 
##        for y<- to length(m_two[1])
##            for x2<-1 to length(m_two)
##                result_multi[x][y] <- result_multi[x][y] + m_one[x][x2] * m_two[x2][y]
##
##
##CALL ADDITION(b,a)
##CALL MULTIPLICATIONWITHNUMBER(result_add,2)
##CALL MULTIPLICATION(b,a)
##CALL SUBTRACTION(result_multi,result_multi_with_number)
