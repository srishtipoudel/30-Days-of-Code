import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve():
    meal_cost = float(input())
    tip_percent = int(input())
    tip=meal_cost * tip_percent / 100
    tax_percent = int(input())
    Tax = meal_cost * tax_percent / 100
    Total = round(meal_cost + tip +Tax)
    print(Total)

solve()
