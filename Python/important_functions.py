def perfectChecker(x):
    sum=0
    for j in range(1,x):
        if x%j==0:
            sum=sum+j
    if(sum==x):
            return True
    return False

def primeChecker(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True
    
def avg(*args):
    return sum(args)/len(args)

# Disclaimer: I have not tested this code!
def gcd(a, b):
    ans = 0
    if a < b:
        min = a
    else:
        min = b
    for i in range(1, min+1):
        if a%i==0 and b%i==0:
            ans = i
    return ans

PI = 3.1415
