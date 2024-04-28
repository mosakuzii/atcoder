n, a, b = map(int, input().split())

count = 0
total = 0
for tmp in range(1, n+1):
  tmp_total = 0
  for tmp2 in list(str(tmp)):
    tmp_total += int(tmp2)
  if tmp_total >= a and tmp_total <= b:
    total += tmp
    count += 1
print(total)