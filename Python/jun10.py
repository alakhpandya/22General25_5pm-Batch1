# Recursion
# It is easy to code a recursive function!
# It is not always possible to have a non-recursive way.

# Factorial using recursion
"""
5! = 5 x 4 x 3 x 2 x 1

5! = 5 x 4!
4! = 4 x 3!
3! = 3 x 2!
2! = 2 x 1!
1! = 1 x 0!

Recursive Step:
n! = n x (n-1)!
Non-Recursive Step
0! = 1      
"""
"""
def recFact(n):
    if n == 0:
        return 1
    else:
        return n * recFact(n-1)
    
print(recFact(7))
"""

# Write a recursive function to compute nth term of an Arithmetic Progression with 'a' as its first term & 'd' as common difference.
"""
a = 6
d = 4
n = 5
AP: 6, 10, 14, 18, 22, 26

Recursive Step:
nth term = (n - 1)th term + d
Non-recursive step:
1st term = a
"""
# Write a recursive function to compute nth term of a Geometric Progression with 'a' as its first term & 'r' as common ratio.
"""
a = 6
r = 4
n = 4
GP: 6, 24, 96, 384
"""

"""
def recGP(a, r, n):
    if n == 1:
        return a
    else:
        return recGP(a, r, n-1) * r
    
# Using above function, write a main program that prints the entire GP upto term 'n'
a = int(input("First Term: "))
r = int(input("Common Ratio: "))
n = int(input("Limit: "))

for x in range(1, n):
    print(recGP(a, r, x), end = ", ")
print(recGP(a, r, x+1))

"""

# Write a recursive program to return nth term of Fibonacci sequence. Also write a main program that takes n from the user and prints all the terms of Fibonacci Sequence till 'n'. Start term number from 1 & Fibonacci sequence as follows:
# 1, 1, 2, 3, 5, 8, 13, 21.....