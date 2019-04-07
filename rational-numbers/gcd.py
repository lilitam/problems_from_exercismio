# def hcfnaive(a,b):
#     if(b==0):
#         return a
#     else:
#         return hcfnaive(b,a%b)
#
# print(hcfnaive(3, -4))

import math
def computeGCD(x, y):
    gcd=1
    if x > y:
        small = y
    else:
        small = x

    for i in range(1, abs(small) + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

print(computeGCD(-4, 8))
print(math.gcd(-4,8))