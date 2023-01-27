#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    number_of_swap = 0
    for i in range(len(a)):
        for j in range(0 , len(a)-i-1):
            if a[j] > a[j+1]:
                number_of_swap = number_of_swap + 1
                a[j] , a[j+1] = a[j+1] , a[j]
                
                
    print("Array is sorted in",number_of_swap,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1]) 
        
        
    
    # Write your code here
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
