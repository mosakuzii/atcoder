a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for a_500 in range(a+1):
  for b_100 in range(b+1):
    for c_50 in range(c+1):
      total = x - (500 * (a_500)) - (100 * (b_100)) - (50 * (c_50))
      if total == 0:
        count += 1

print(count)