len_num = int(input())
nums = map(lambda x: int(x), input().split())
a = 0
b = 0
for i, n in enumerate(nums):
  if i == 0:
    a = n
  elif i == 1:
    if n > a:
      b = a
      a = n
    else:
      b = n
  else:
    if n >= a:
      b = a
      a = n
    elif n > b:
      b = n
  
print(a * b)