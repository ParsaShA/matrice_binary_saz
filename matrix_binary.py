def binary_matrix(n,m):
    matrice = [  [0]*m for _ in range(n)         ]
    for i in range(n):
        for j in range(m):
            if i%2==0:
                matrice[i][j] = 1
            else:
                if j%2==1:
                    matrice[i][j]=1
    return matrice
print(binary_matrix(4,4))