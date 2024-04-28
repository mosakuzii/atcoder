n = int(input())
ans = input().split()
int_ans = sorted([int(an) for an in ans], reverse=True)

alice_score = 0
bob_score = 0
for i in range(0,n):
  if i%2 == 0:
    alice_score += int_ans[i]
  else:
    bob_score += int_ans[i]

print(alice_score-bob_score)