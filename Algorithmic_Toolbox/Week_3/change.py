#!/usr/bin/env python3

pay = int(input())
change_coins = 0

for n in [10, 5, 1]:
    while pay - n >= 0:
        change_coins += 1
        pay -= n

print(change_coins)