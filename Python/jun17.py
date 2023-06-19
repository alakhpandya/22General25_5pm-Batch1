# Explicit Memoization
"""
cache_memory = {}
def fabonacci(n):
    if n in cache_memory:
        return cache_memory[n]
    if n == 1 or n == 2:
        cache_memory[n] = 1
        return 1
    else:
        t = fabonacci(n-1) + fabonacci(n-2)
        cache_memory[n] = t
        return t
a = 1
b = 1
count = 0
x = int(input("n: "))   # 1000
for i in range(1,x+1):
    count+=1
    print(count,":",fabonacci(i),end="\n")
print(cache_memory)
"""

# cache_memory = {"Physics":50, "Maths":49, "C":48}
# print(cache_memory.keys())
# print(cache_memory["Maths"])
# cache_memory = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13}
# print(cache_memory[6])
# test = int(input("Key: "))
# if test in cache_memory:
#     print("present")


# Implicit Memoization
"""
from functools import lru_cache

# Decorators/Wrapper Function
# @lru_cache(maxsize=1000)
@lru_cache(maxsize=3)
def recfibbo(n):
    if n==1 or n==2:
        return 1 
    else:
        return recfibbo(n-1)+recfibbo(n-2)

fib=int(input("enter fibbo:"))

for i in range (1,fib+1):
        print(f"{i}. {recfibbo(i)}")
"""

# Organizing our code in Modules & Packages
"""
import important_functions

print(important_functions.prime(135))
"""
"""
import important_functions as imp

print(imp.avg(20,30))
"""
# import speech_recognition as sr
# import numpy as np
# import pandas as pd
"""
import important_functions as imp

r = int(input("r: "))
area = imp.PI * r ** 2
print(area)
"""
"""
from important_functions import avg, perfectChecker as pc, gcd

print(avg(4,5))
print(pc(28))
"""

from important_functions import *

print(perfectChecker(28))

# Next Class: Packages