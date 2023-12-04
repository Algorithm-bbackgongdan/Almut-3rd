import sys

N, P = map(int, sys.stdin.readline().rstrip().split())
melodys = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

answer = 0
stacks = [[] for _ in range(N+1)]
for n, p in melodys:
  if len(stacks[n]) == 0 or stacks[n][-1] < p:
    answer += 1
    stacks[n].append(p)
  elif p < stacks[n][-1]:
    while stacks[n] and p < stacks[n][-1]:
      stacks[n].pop()
      answer += 1
    if len(stacks[n]) == 0 or stacks[n][-1] < p:
      stacks[n].append(p)
      answer += 1
print(answer)