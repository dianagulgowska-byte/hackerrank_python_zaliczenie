#2Characters poprawione
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

#funkcja sprawdza max dlugosc naprzemiennego ciagu liter zlozonego z l1,l2
def check_letter_pair(k, l1, l2):
    z = ""
    for i in range (len(k)):
        if k[i] == l1 or k[i] == l2:
            z += k[i]
    
    t = ""
    for i in range (len(z)-1):
        if z[i] == z[i+1]:
            return 0
        t += z[i]
    t += z[len(z)-1]
    
    return len(t)
    
    
    
def alternate(s):
    # Write your code here

    #zliczamy ile razy wystepuje kazda litera, sortujemy malejaco
    licznik_liter ={}
    for l in s:
        licznik_liter[l] = licznik_liter.get(l,0)+1
        
    licznik_liter = dict(sorted(licznik_liter.items(),key = lambda item:item[1], reverse=True))
   

    
    max_x = 0
    key_list = list(licznik_liter.keys())
    for i in range (len(key_list)-1):
        for j in range (i+1, len(key_list)):
            if 2*licznik_liter[key_list[j]] + 1 < max_x:
                continue
            x = check_letter_pair(s, key_list[i], key_list[j])
            if x > max_x:
                max_x = x
                
    
    
    return max_x
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
