#!/usr/bin/env python
number = 600851475143
divisors = list()
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        divisors.append(i)

for i in range(len(divisors)):
    n = divisors[-1 - i]
    if all(n % d != 0 for d in divisors if d != n):
        print(n)
        break
