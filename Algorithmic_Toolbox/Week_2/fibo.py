#!/usr/bin/env python3

n = int(input())
a = 0
b = 1
i = 0
while i < n:
    t = a
    a += b
    b = t
    i += 1
print(a)
