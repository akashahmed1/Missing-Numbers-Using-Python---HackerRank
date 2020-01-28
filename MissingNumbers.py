#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def CountFrequency(arr): 
    return collections.Counter(arr)
# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
  
    freq = CountFrequency(sorted(brr))
    hashMap = {} 

    for key, value in freq.items(): 
        hashMap[str(key)] = value;

    for x in (sorted(arr)):
        if (str(x) in hashMap): 
            hashMap[str(x)] = hashMap[str(x)]-1

            if(hashMap[str(x)] == 0):
                del hashMap[str(x)]

    finalList = list(hashMap.keys())
    return (finalList)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
