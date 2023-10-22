N, H = map(int,input().split())

dungeon = []
result = []

for _ in range(N):
  info = list(map(int,input().split()))
  dungeon.append(info)

attack = H
for i in range(len(dungeon)):
  if dungeon[i][0] == 1:
    quotient = dungeon[i][2] // attack
    rest = dungeon[i][2] % attack
    if rest == 0:
      answer = (quotient - 1) * dungeon[i][1]
      result.append(-answer)
    else:
      answer = quotient * dungeon[i][1]
      result.append(-answer)
  else:
    attack += dungeon[i][1]
    result.append(dungeon[i][2])

result.sort(reverse=True)

hp = 0
for i in range(len(result)-1):
  hp += result[i]

if hp >= 0:
  print(-result[N-1] + 1)
else:
  print(-result[N-1] + hp + 1) 