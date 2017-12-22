#!/usr/bin/env python
def factorize(n):
    factors = [0 for i in range(21)]
    i = 2
    while (n != 1):
        if n % i == 0:
            factors[i] += 1
            n = n // i
        else:
            i += 1
    return factors


numbers = range(2, 21)
factors = [max(col) for col in zip(*[factorize(n) for n in numbers])]

res=1
for n in numbers:
    res *= n**factors[n]

print(res)