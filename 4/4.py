#!/usr/bin/env python
n_digits = 0


def left(n, i):
    return n // (10 ** (n_digits - i - 1)) % 10


def right(n, i):
    return n // (10 ** i) % 10


def digits(n):
    res = 0
    while (n > 0):
        n = n // 10
        res += 1
    return res


max_palindrome = 10201
for i, j in [(i, j) for i in range(100, 1000) for j in range(100, 1000)]:
    n = i * j
    n_digits = digits(n)
    if all(left(n, j) == right(n, j) for j in range(0, n_digits)):
        max_palindrome = max(max_palindrome, n)

print(max_palindrome)
