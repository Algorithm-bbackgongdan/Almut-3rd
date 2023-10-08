# WEEK 1

## BOJ 21758
### Code
```python
from sys import stdin

def solution(n, numbers):
    # bee1 ... bee2 ... goal
    answer = 0
    sums = [numbers[0]]

    bee1 = 0
    bee2 = 1
    goal = n - 1

    for i in range(1, n):
        sums.append(sums[i-1] + numbers[i])

    while bee2 < goal:
        answer = max(answer, sums[goal] - sums[bee1] + sums[goal] - sums[bee2] - numbers[bee2])
        bee2 += 1

    # bee1 ... goal ... bee2
    bee1 = 0
    bee2 = n - 1
    goal = 1

    while goal < bee2:
        answer = max(answer, sums[goal] - sums[bee1] + sums[bee2 - 1] - sums[goal - 1])
        goal += 1

    # goal ... bee1 ... bee2

    bee1 = n - 2
    bee2 = n - 1
    goal = 0

    while bee1 > goal:
        answer = max(answer, sums[bee1 - 1] + sums[bee2 - 1] - numbers[bee1])
        bee1 -= 1

    return answer


n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))

print(solution(n, numbers))

```

### Approach
1. 음 딱 봐도 벌이랑 벌통을 끝으로 몰아야겠네
2. 근데 예시를 보니깐 그게 아니네..?
3. 그럼 `벌 ... 벌 ... 벌통`, `벌 ... 벌통 ... 벌`, `벌통 ... 벌 ... 벌` 세 가지로 나눠야겠다.
4. `벌` `벌` `벌통` 중 두 개는 무조건 양 끝에 고정이고, 나머지 하나를 합을 최대로 만드는데 배치해야 한다.
5. 그 위치를 찾아서 최대값을 구하자!

### TIL
세 가지 케이스로 나누는 건 금방 했는데 누적합 배열을 만들지 않아서 시간 초과가 발생했다.
사실 나도 풀면서.. `10^5 * 10^5`가 발생할 수도 있겠다 생각했는데 정신승리(...)로 그냥 제출했다. 여기서 배운 건
1. 시간 초과가 발생할지 **꼼꼼하게** 체크하자
2. 누적합 스멜이 나면 누적합 배열을 만들자

## BOJ 2174
### Code
```python
 from sys import stdin

directions = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
    0: 'N',
    1: 'E',
    2: 'S',
    3: 'W'
}

def mapPosition(x, y):
    return n - y, x - 1


def rotate(curDir, dir, num):
    num %= 4

    if dir == 'L':
        return directions[(directions[curDir] - num) % 4]
    else:
        return directions[(directions[curDir] + num) % 4]

def moveForward(pos, dir, num):
    # Return Description
    # 1. 벽 밖으로 벗어난 경우 -> -1, -1
    # 2. 로봇에 부딪힌 경우 -> -1, 부딪힌 로봇 번호
    # 3. 정상적으로 이동한 경우 -> newx, newy

    x, y = pos
    board[x][y] = 0
    i = 1

    if dir == 'N':
        while i <= num:
            x -= 1
            if x < 0:
                return -1, -1
            if board[x][y]:
                return -1, board[x][y]
            i += 1

    elif dir == 'E':
        while i <= num:
            y += 1
            if y >= m:
                return -1, -1

            if board[x][y]:
                return -1, board[x][y]
            i += 1

    elif dir == 'S':
        while i <= num:
            x += 1
            if x >= n:
                return -1, -1
            if board[x][y]:
                return -1, board[x][y]
            i += 1

    else:
        while i <= num:
            y -= 1
            if y < 0:
                return -1, -1
            if board[x][y]:
                return -1, board[x][y]
            i += 1

    return x, y

def solution():
    for robot, comType, repeat in commands:
        x, y, dir = robots[robot]
        if comType == 'F':
            x, y = moveForward((x, y), dir, repeat)

            if x == -1:
                if y == -1:
                    return "Robot " + str(robot) + " crashes into the wall"
                else:
                    return "Robot " + str(robot) + " crashes into robot " + str(y)
            robots[robot] = [x, y, dir]
            board[x][y] = robot

        else:
            dir = rotate(dir, comType, repeat)
            robots[robot] = [x, y, dir]

    return 'OK'

m, n = map(int, stdin.readline().split())
a, b = map(int, stdin.readline().split())
robots = [[]]
commands = []
board = [[0 for _ in range(m)] for _ in range(n)]

for index in range(1, a + 1):
    x, y, dir = stdin.readline().split()
    x, y = mapPosition(int(x), int(y))
    
    robots.append([int(x), int(y), dir])
    board[x][y] = index

for _ in range(b):
    robot, comType, repeat = stdin.readline().split()
    commands.append([int(robot), comType, int(repeat)])

print(solution())

```
### Approach
1. 주어진대로 구현만 잘 하면 되겠다.
2. 다만, 전진하다가 다른 로봇에 부딪힌 경우를 생각하기 위해 `0`으로 초기화된 `board`라는 2차원 배열을 만들자
3. `board`의 각 로봇이 위치한 곳에 `index`를 저장하자
4. 로봇이 움직이다가 `0`이 아닌 값을 만나면 로봇이랑 부딪힘!!
   
### TIL
구현 문제는 누가 누가 더 꼼꼼하냐인 듯하다. `moveForward()` 함수를 호출한 다음, `board`에서 새로운 위치로 갱신을 안해줘서 틀렸다 🥲

이번 문제를 풀면서 느낀 점은 제발 좀 꼼꼼하자. 코테는 다시 제출하기가 없다.
