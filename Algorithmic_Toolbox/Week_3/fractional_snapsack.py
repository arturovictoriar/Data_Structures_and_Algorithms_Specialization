#!/usr/bin/env python3

number_L_and_W = input().split(" ")
n = int(number_L_and_W[0])
W = int(number_L_and_W[1])

list_items = []
while n != 0:
    v_w = input().split(" ")
    list_items.append([int(v_w[0]), int(v_w[1])])
    n -= 1

s_list_items = sorted(list_items, key=lambda x: (x[0] / x[1]), reverse=True)

max_fraction = 0
for i in s_list_items:
    if not W:
        break
    if W - i[1] >= 0:
        max_fraction += i[0]
        W -= i[1]
    else:
        max_fraction += ((i[0] * W) / i[1])
        W = 0

print("{:.4f}".format(max_fraction))
