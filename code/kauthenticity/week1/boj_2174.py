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
