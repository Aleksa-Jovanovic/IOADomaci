import numpy as np
from scipy import special




def func(left, right, n):
    while left <= right:
        mid = (left + right) / 2
        res = special.spherical_jn(n, mid)
        if (right - left) / 2 < 10e-12 or res == 0:
            return mid
        elif np.sign(res) == np.sign(special.spherical_jn(n, left)):
            left = mid
        else:
            right = mid




left = [4, 7.5, 5.5, 9]
right = [5, 8, 6, 9.4]

n = 1
result = 1
for x in range(4):
    if x > 1 :
        n = 2
    if x % 2 == 0:
        result = 1
    else:
        result = 2
        
    print("For N = " + str(n) + " => result(" + str(result) + ") = " + str(func(left[x], right[x], n)))


