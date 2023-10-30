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

result.sort()

hp = 0
for i in range(len(result)):
  hp += result[i]

if hp > result[0]:
  min_hp = -result[0] + 1
else:
  min_hp = -hp + 1

print(min_hp)
