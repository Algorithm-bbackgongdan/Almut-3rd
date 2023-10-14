# WEEK 2

## BOJ 2573
### Code
```python
from sys import stdin
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def meltIceberg():
    global n, m, board
    meltings = [] # (row, col, cnt)

    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                continue

            cnt = 0 # 주변 바다의 개수

            for dirX, dirY in directions:
                newX, newY = x + dirX, y + dirY

                if newX < 0 or newX >= n or newY < 0 or newY >= m:
                    continue

                if board[newX][newY] == 0:
                    cnt += 1

            if cnt > 0:
                meltings.append((x, y, cnt))

    for row, col, cnt in meltings:
        board[row][col] = max(0, board[row][col] - cnt)

    return

def solution():
    global n, m, board

    answer = 0

    sea = 0
    for row in board:
        sea += row.count(0)

    # 바다가 없어서 녹지 못함
    if sea == 0:
        return 0

    while True:
        visited = set()
        icebergCnt = 0

        # 빙산의 개수 카운트
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 or (i, j) in visited:
                    continue

                queue = deque([])

                visited.add((i, j))
                queue.append((i, j))
                icebergCnt += 1

                while queue:
                    curX, curY = queue.popleft()

                    for dirX, dirY in directions:
                        newX, newY = curX + dirX, curY + dirY

                        if newX < 0 or newX >= n or newY< 0 or newY >=m or (newX, newY) in visited or board[newX][newY] == 0:
                            continue

                        queue.append((newX, newY))
                        visited.add((newX, newY))
        
        # 빙산이 분리됨
        if icebergCnt >= 2:
            break

        # 다 녹아서 없음
        elif icebergCnt == 0:
            answer = 0
            break

        meltIceberg()
        answer += 1

    return answer


n, m = map(int, stdin.readline().rstrip().split())
board = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

print(solution())

```
### Approach
1. BFS로 빙산 개수 카운트한다.
2. 빙산 개수가 2개 이상이면 멈추자.
3. 2차원 배열 돌면서 바다랑 접한 면의 개수를 카운트한다.
4. 빙하 녹인다.
5. 1로 돌아간다.
   
### TIL
바다가 없어서 빙하가 녹지 못하는 건 생각했지만, 빙하가 다 녹아버려서 빙산이 0개가 되는 건 생각하지 못했다ㅠㅠ
이런 엣지 케이스를 생각해내는 건 문제를 많이 풀어보는 수밖에 없는건지 고민이 된다

## BOJ 2470
### Code
```python
from sys import stdin
def solution():
    global n, numbers

    answer = []
    low, high = 0, n - 1
    minVal = float('inf')

    numbers.sort()

    while low < high:
        if abs(numbers[low] + numbers[high]) < minVal:
            minVal = abs(numbers[low] + numbers[high])
            answer = [numbers[low], numbers[high]]

            if minVal == 0:
                break

        if numbers[low] + numbers[high] < 0:
            low += 1
        elif numbers[low] + numbers[high] > 0:
            high -= 1

    return answer


n = int(input())
numbers = list(map(int, stdin.readline().rstrip().split()))
a, b = solution()
print(a, b)

```
### Approach
1. 두 수의 합을 최대한 0에 가깝게 만들어야 한다.
2. 그래서 만약에 합이 음수면, 0에 가깝게 되도록 두 수 중 한 개를 키워야 한다.
3. 합이 양수면 두 수 중 한 개를 줄여야 한다.
4. 따라서 숫자들을 정렬하고 `low = 0`, `high = n-1`로 투 포인터를 두자.
5. `numbers[low] + numbers[high] < 0` -> `low += 1`
6. `numbers[low] + numbers[high] > 0` -> `high -= 1`
7. `low >= high`가 되면 종료
   
### TIL
처음에는 문제를 그리디하게 풀어서 실패했다. 웬만해선 그리디가 먹히기 어렵다는 걸 기억하자..
결국에는 풀이를 봤다. `0`에 가깝게 만드는 것이 목적이므로 무조건 0에 가까워지는 방법에 따라 투포인터를 움직여야 한다.


## Programmers 43163
### Code
```python
from collections import deque

MAX_NUM = 1000000000000

def isChangable(a, b) : 
    diff = 0
    
    for i in range(len(a)) : 
        if a[i] != b[i] : 
            diff += 1
        
        if diff == 2 :
            return False
    
    return True

def solution(begin, target, words):
    answer = MAX_NUM
    visited = {}
    
    for word in words : 
        visited[word] = False
        
    queue = deque([(begin, 0)])
    
    while queue : 
        cur, cnt = queue.popleft()
        
        if cur == target : 
            answer = cnt
            break
            
        for word in words : 
            if visited[word]:
                continue

            if isChangable(cur, word):
                queue.append((word, cnt + 1))
                visited[word] = True

    return 0 if answer == MAX_NUM else answer
```
### Approach
1. 현재 단어에서, 바꿀 수 있는 단어로 하나씩 변환해 가면서 큐에 넣는다.
2. 바꿀 수 있는의 뜻은, 현재 단어와 바꿀 단어가 오직 한 글자만 다르다는 것
3. 이떄 이미 방문했던 단어는 더 방문하지 않는다. 왜냐하면 이미 그 단어로 변환한 적이 있기 때문에 또 할 필요가 없다.

### TIL
크게 어렵지는 않았던 것 같다. 다만 이미 변환한 적이 있는 단어에 대해서는 또 다시 검사하지 않음을 체크하는게 미묘한 것 같다.
