# boj_30619 : 내 집 마련하기
### code
```python
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
  
  ```
## 결과
### 성공
## 접근
높은 번호의 집에, 높은 번호의 사람이 살아야 감면받을 수 있는 세금이 커진다.

따라서 L번부터 R번까지의 사람이 번호 순으로 높은 번호의 집에 살 때 가장 많은 세금을 감면 받을 수 있다.

1. 주어진 수열에서 L에서 R번 사이 번호사람을 따로 뽑아 번호 역순으로 정렬 시킨다. 그리고 새로 정렬될 수열('relocation_houses')에 L에서 R번 사이의 사람이 살던 집을 0으로 초기화 한다.
2. 이후 재배열 되는 수열에 번호 순서대로 사람을 재배치 시킨다.
## 문제 회고
처음에 문제 이해가 한번에 되지않아 당황했다.
수열에서 인덱스와 값이 의미하는 것을 이해하고, 어렵지않게 정렬을 통해 문제를 해결할 수 있었다.

# boj_30618 : donstructive 
### code
```python
import sys

n = int(sys.stdin.readline().rstrip())
answer = [0 for _ in range(n+1)]

if (n % 2 == 0):
  for i in range(n//2):
    answer[i] = 2 * i + 1 #홀수
    answer[i + n//2] = n - (2*i) #짝수

else:
  for i in range(n//2+1):
    answer[i] = 2 * i + 1
    answer[i + (n//2+1)] = (n-1) - (2*i)

for i in range(len(answer) - 1):
  print(answer[i], end=" ")

  ```
## 결과
### 성공
## 접근
순열의 점수는 연속 부분 수열의 원소들의 합을 모두 더한 값이기 때문에 가장 큰 N이 최대한 많이 중복되어 더해져야 한다고 생각했다.

N = 3, 4, 5 일 때, 순열의 인덱스에 따라 중복되는 횟수를 확인해보았다.

N = 3일 때는 순열의 원소 위치(인덱스)에 따라 3번, 4번, 3번 (3, 4, 3)

N = 4일 때는 4번, 6번, 6번, 4번 (4, 6, 6, 4)

N = 5일 때는 5번, 8번, 9번, 8번, 5번 숫자가 중복됨을 확인했다. (5, 8, 9, 8, 5)

순열의 가운데를 기준으로 중복 횟수가 대칭임을 확인하고, 큰 수를 순열의 가운데에 위치시키고자 하였다.
이후, 순열 가운데를 기준으로 양쪽에 수를 번갈아가며 배치 시켰다.

N = 5 일 때, 순열의 배치
| index | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 값 | 1 | 3 | 5 | 4 | 2 |

N = 6 일 때, 순열의 배치
| index | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 값 | 1 | 3 | 5 | 6 | 4 | 2 |

순열을 배치하고 보니 순열의 중앙을 기준으로 홀수와 짝수로 나눠져 배치되는 것을 확인할 수 있었다.
그래서 N값이 홀수일 때와 짝수일 때로 나눠 위의 규칙에 맞게 원소를 배치시켰다.

## 문제 회고
비교적 빠른 시간에 규칙을 찾았다. 하지만 코드로 구현하는 과정 중, 순열의 중앙값 이후 짝수를 배치하기 위해 인덱스와 값 사이의 연관성을 찾는 과정이 꽤 어려웠다.


# 2589 : 보물섬
### code
```python
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

treasure_map = []

# N E S W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#보물지도 그래프
for i in range(n):
  arr = []
  words = (sys.stdin.readline().rstrip())

  for word in words:
    arr.append(word)
  
  treasure_map.append(arr)

def BFS(treasure_map, x, y):
  visited = [[0 for _ in range(m)] for _ in range(n)]
  count = 0
  queue = deque()
  visited[x][y] = 1
  queue.append((x,y))

  while queue:
    a, b = queue.popleft()
  
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if (nx < 0 or nx >= n or ny < 0 or ny >= m):
        continue
      elif(treasure_map[nx][ny] == 'L' and visited[nx][ny] == 0):
        visited[nx][ny] = visited[a][b] + 1
        count = max(count, visited[nx][ny])
        queue.append((nx,ny))

  return count-1

result = 0
for i in range(n):
  for j in range(m):
    if treasure_map[i][j] == 'L':
      result = max(result, BFS(treasure_map,i,j))

print(result)


  ```
## 결과
### 실패 후 참조
## 접근
1. 보물지도를 완전탐색하여 처음 육지를 탐색한 순간, BFS 함수를 실행한다.
2. BFS 함수는 시작 육지 'L'과 다른 육지 'L'사이의 최대 이동시간을 저장한다.
3. 그 후, result에 다른 위치에서 시작한 이동시간과 2번값을 비교하여 큰 값을 저장하고 출력한다.
## 문제 회고
처음에는 최단거리가 가장 긴 노드사이의 거리를 구하기위해 깊이를 구하는 것으로 이해하고 DFS를 사용하였다.
하지만 육지를 멀리 돌아가는 경우가 발생하였다. 이를 잡기 위해 counts 리스트를 만들고, 이동시간을 min함수를 이용해 저장해보는 등 많은 시도를 해보았지만 결국 멀리 돌아가는 경우를 잡지 못하였다.

결국 구글 코드를 참조하였고, 2차원 리스트의 경우 넓이 우선 탐색(BFS)을 통해 최단거리를 구하면 멀리 돌아가는 경우를 잡을 수 있음을 깨달았다...

문제 상황에 따른 DFS, BFS 적용을 좀 더 세심하게 공부할 필요가 있을 것같다.