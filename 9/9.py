#!/usr/bin/env python
N=1000

for c in range(1,N+1):
    for b in range(1,c):
        for a in range(1,b):
            if a+b+c == N:
                if a**2 + b**2 == c**2:
                    print(a*b*c)