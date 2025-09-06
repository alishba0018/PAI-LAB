x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
z=[[1,2],[3,4],[5,6]]
result1=[[0,0,0],[0,0,0],[0,0,0]]
result2=[[0,0],[0,0],[0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result1[i][j]=x[i][j]+y[i][j]
    
for i in range(len(x)):
    for j in range(len(z[0])):
        for k in range(len(z)):
            result2[i][j]+=x[i][k]*z[k][j]

    
print("Matrix X:")
print(x)
print("Matrix Y:")
print(y)
print("\nAddition of X and Y:")
for r in result1:
    print(r)
print("\nMultiplication of X and Z:")
for r in result2:
    print(r)   
