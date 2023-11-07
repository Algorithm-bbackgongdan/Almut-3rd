N, H = map(int,input().split())

dungeon = []

for _ in range(N):
  info = list(map(int,input().split()))
  dungeon.append(info)

left = 1
right = N * 1000000000000
answer = 0

while (left <= right):
  mid = (left + right) // 2
  HP = mid
  attack = H

  for i in range(len(dungeon)):

    if dungeon[i][0] == 1:
      quotient = dungeon[i][2] // attack
      rest = dungeon[i][2] % attack
      if rest == 0:
        HP -= dungeon[i][1] * (quotient-1)
      else:
        HP -=dungeon[i][1] * quotient
      if HP <= 0:
          break
    
    else:
      attack += dungeon[i][1]
      HP += dungeon[i][2]
      if HP > mid:
        HP = mid
  
  if HP > 0:
    right = mid -1
    answer = mid
  else:
    left = mid + 1

print(answer)