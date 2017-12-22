#!/usr/bin/env python
nth_prime = 10001


def is_prime(n):
    n_sqrt_root = int(n**0.5)
    return all(n % p != 0 for p in primes if p<=n_sqrt_root)


primes = [2]
n = 3
while len(primes) < nth_prime:
    if is_prime(n):
        primes.append(n)
    n += 2

print(primes[-1])
