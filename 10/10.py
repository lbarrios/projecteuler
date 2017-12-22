#!/usr/bin/env python
n_max = 2000000


def is_prime(n):
    n_sqrt_root = int(n ** 0.5)
    for p in primes:
        if p > n_sqrt_root:
            break
        if n % p == 0:
            return False
    return True


primes = [2]
n = 3
while n < n_max:
    if is_prime(n):
        primes.append(n)
    n += 2

print(sum(primes))
