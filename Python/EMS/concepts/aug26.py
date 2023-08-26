"""
class A:
    __performance = 3       # private


a = A()
# print(a.__performance)

# Name mangling
print(a._A__performance)
"""
class Complex():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def __add__(self, q):
        r = self.real + q.real
        i = self.imag + q.imag
        result = Complex(r, i)
        return result

a = Complex(3, 4)   # 3 + 4j
b = Complex(2, 5)   # 2 + 5j
c = a + b
print(c.real, "+", c.imag, "\bj")

p = 5
p.__add__