import sys
import copy

n = int(sys.stdin.readline().rstrip())
houses = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

for i in range(m):
  people = []
  l, r = map(int,sys.stdin.readline().rstrip().split())
  relocation_houses = copy.deepcopy(houses)
  for j in range(len(houses)):
    if (l <= houses[j] <= r):
      people.append(houses[j])
      relocation_houses[j] = 0
  
  people.sort(reverse= True)

  for j in range(len(relocation_houses)):
    if relocation_houses[j] == 0:
      relocation_houses[j] = people[-1]
      people.pop()
      
  for house in relocation_houses:
    print(house, end=' ')
  