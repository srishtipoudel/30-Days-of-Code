#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalnumberofSwaps=0
for i in range(n):
    numberofSwaps=0
    for j in range(n-1):
        if a[j]>a[j+1]:
            tmp=a[j]
            a[j]=a[j+1]
            a[j+1]=tmp
            numberofSwaps+=1
    totalnumberofSwaps+=numberofSwaps
    if numberofSwaps==0:
        break    

print('Array is sorted in ' + str(totalnumberofSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))
