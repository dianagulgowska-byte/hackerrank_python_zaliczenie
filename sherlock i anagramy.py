#sherlock i anagramy
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def czy_anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        return 1
    return 0 
    
    
def sherlockAndAnagrams(s):
    # Write your code here
    licznik = 0
    for l in range(1,len(s)):
        for i in range(len(s)-l+1):
            for j in range(i+1, len(s)-l+1):
                licznik += czy_anagram(s[i:i+l], s[j:j+l])
            
            
    return licznik
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
