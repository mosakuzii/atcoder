n = int(input())
ans = input().split()
int_ans = [int(an) for an in ans]

count = 0
tmp_ans = int_ans
enable2div_flag = True

while(enable2div_flag):
  next_ans = []
  for tmp_an in tmp_ans:
    if tmp_an%2 == 0:
      next_ans.append(int(tmp_an/2))
    else:
      enable2div_flag = False
      break
  
  if enable2div_flag:
    count += 1
    tmp_ans = next_ans
    continue
  else:
    break
print(count)