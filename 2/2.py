#!/usr/bin/env python
fibs = [0, 1]
while (fibs[-1] < 4000000):
    fibs.append(fibs[-2] + fibs[-1])

print(sum([i for i in fibs if i % 2 == 0]))
