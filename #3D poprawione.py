#3D poprawione
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#



def surfaceArea(A):
    # Write your code here
    
    W = len(A)
    H = len(A[0])
    
    
    # funkcja porownaj sasiadow, sprawdza roznice w wysokosciach kolumn u sasiednich pozycji(i1,j1) oraz (i2,j2)
    def porownaj_sasiadow(i1, j1, i2,j2):
        if i2<0 or j2<0 or i2>= W or j2 >= H:
            return A[i1] [j1] 
        if A [i1][j1] > A [i2] [j2]:
            return A [i1] [j1] - A [i2] [j2]
        return 0 
    
    pole = 0

        
    #liczymy kom wewnetrzne
    for i in range(0,W):
        for j in range(0,H):
            p = 1+1 +porownaj_sasiadow(i,j,i-1,j) + porownaj_sasiadow(i,j,i,j-1) + porownaj_sasiadow(i,j,i+1,j)+porownaj_sasiadow(i,j,i,j+1)
            pole += p
    
    
    return pole

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
