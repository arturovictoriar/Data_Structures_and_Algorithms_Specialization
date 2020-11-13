#!/usr/bin/env python3

n = input().split(" ")
if n[1] > n[0]:
    a = int(n[1])
    b = int(n[0])
else:
    a = int(n[0])
    b = int(n[1])

while a % b != 0:
    t = a
    a = b
    b = t % b

print(int((int(n[0]) * int(n[1])) / b))
