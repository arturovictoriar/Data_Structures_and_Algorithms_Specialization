#!/usr/bin/env python3

d = int(input())
m = int(input())
n_s = int(input())
list_s = list(map(lambda x: int(x), input().split(" ")))
total_number_station = 0
last_s = 0
flag = 0
i = 0
while i < len(list_s) and m + last_s < d:
    prev_i = i
    while i < len(list_s) and list_s[i] <= m + last_s:
        i += 1
    if prev_i == i:
        flag = 1
        break
    total_number_station += 1
    i -= 1
    last_s = list_s[i]
    i += 1

if flag or m + last_s < d:
    print(-1)
else:
    print(total_number_station)
