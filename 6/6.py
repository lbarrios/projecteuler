#!/usr/bin/env python
first_100_nat = list(range(1, 101))
first_100_nat_squares = list(map(lambda x: x**2, first_100_nat))

print(sum(first_100_nat)**2 - sum(first_100_nat_squares))