

def add_matrix(X,Y):
    result = [[X[i][j] + Y[i][j]  for j in range (len(X[0]))] for i in range(len(X))]
    return result

#X = [[1,2]]
#Y = [[2,3]]

X = [[1,2]]

Y = [[2,3]]

X1 = [[1,2,3],
     [4,5,6]]

Y1 = [[1,1,1],
     [2,2,2]]
assert add_matrix(X,Y)==[[3,5]]
assert add_matrix([1,2],[2,3])==[3,5]
assert add_matrix(X1,Y1)==[[2,3,4],[6,7,8]]


