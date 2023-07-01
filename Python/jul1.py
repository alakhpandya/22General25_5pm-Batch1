"""
import datetime

hetvi = datetime.datetime(2023, 10, 2)
# print(hetvi)
# strftime
hetvi_bday = hetvi.strftime("%B %d, %Y (%a)")

# October 2, 2023 (Thu)
# 2nd October 2023, Thursday
# Thursday, 2nd October 2023
print(hetvi_bday)
"""

# strptime
"""
from datetime import datetime, date, time, timedelta

chandrayaan2 = "22 July 2019 at 2.43 PM"
c2 = datetime.strptime(chandrayaan2, "%d %B %Y at %I.%M %p")
print(c2)


# time module

import time
from functools import lru_cache

# print(dir(time))
# starting from 1st january 1970
# print(time.time())

# @lru_cache(maxsize=3)
@lru_cache()
def recfibbo(n):
    if n==1 or n==2:
        return 1 
    else:
        return recfibbo(n-1)+recfibbo(n-2)

t1 = time.time()
for x in range(1, 100001):
    recfibbo(x)
t2 = time.time()
exe_time = t2 - t1
print("Execution time =", exe_time)
"""
# Write a program that checks time take to create 1 billion such lists and 10 million such sets and show the time taken for both the tasks and print which one is faster.
"""
import time
print("Started...")
start1 = time.time()
for x in range(100):
    l1=[i for i in range(1,1000001)]
end1 = time.time()
list_time = end1 - start1

start2 = time.time()
for x in range(100):
    l1={i for i in range(1,1000001)}
end2 = time.time()
set_time = end2 - start2

print("List time:", list_time)
print("Set time:", set_time)
"""
"""
import time
t1=time.time()
for j in range(1,10001):
    l = [i for i in range(1,10001)]
t2=time.time()
t3=t2-t1
print(t3)

t1=time.time()
for j in range(1,10001):
    l = {i for  i in range(1,10001)}
t2=time.time()
t3=t2-t1
print(t3)
"""
"""
from timeit import timeit

list_time = timeit("l = [i for i in range(1,10001)]", number=10000)
set_time = timeit("s = {i for i in range(1,10001)}", number=10000)

print(list_time)
print(set_time)
"""