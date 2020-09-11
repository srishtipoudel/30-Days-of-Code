import math
import os
import random
import re
import sys




n = int(input())
current_consecutive_is=0
max_consecutive_is=0
while n>0:
    remainder= n%2
    if remainder==1:
        current_consecutive_is+=1
        if current_consecutive_is > max_consecutive_is:
            max_consecutive_is=current_consecutive_is
    else:
        current_consecutive_is=0
    n=n//2

print(max_consecutive_is)    
