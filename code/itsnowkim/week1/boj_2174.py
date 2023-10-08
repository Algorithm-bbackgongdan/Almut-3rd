import sys
from sys import stdin
input = stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
dirInfo = {"N": 0, "S": 1, "W": 2, "E": 3}
changeDir = {"L" : (2, 3, 1, 0), "R": (3, 2, 0, 1)}

# 로봇 이동 함수 - (번호, 명령어, 반복 횟수) 정보 인자로 받음
def moveRobot(num, cmd, cnt):
    global robotInfo, posInfo
    r, c, d = robotInfo[num]    # 현재 로봇 위치, 방향
    
    # 회전 명령 - L 또는 R 방향으로 90도로 cnt번 회전  
    if cmd in "LR":
        cnt %= 4        # 4번 돌면 제자리이므로 4로 나눈 나머지를 취함
        for _ in range(cnt):
            d = changeDir[cmd][d]
        nd = d
        robotInfo[num][2] = nd       # 새로운 방향 등록 

    # 직진 명령 - d방향으로 cnt칸 만큼 이동
    else:
        del robotInfo[num]          # 해당 로봇 정보 삭제
        del posInfo[(r, c)]         # 해당 위치 정보 삭제
        for _ in range(cnt):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < R and 0 <= nc < C):           # 격자 밖으로 나가면
                print("Robot", num, "crashes into the wall")
                sys.exit()
            
            elif (nr, nc) in posInfo.keys():                # 놓여있는 로봇과 충돌하면
                print("Robot", num, "crashes into robot", posInfo[(nr, nc)])
                sys.exit()
            r, c = nr, nc

        # 이동한 로봇 정보 새로 등록
        robotInfo[num] = [r, c, d]
        # 이동한 위치 정보 새로 등록
        posInfo[(r, c)] = num

# main
if __name__ == "__main__":
    C, R = map(int, input().split())
    N, M = map(int, input().split())

    robotInfo = dict()
    posInfo = dict()
    for n in range(1, N+1):
        x, y, d = list(input().split())
        sr = R-int(y)
        sc = int(x)-1
        robotInfo[n] = [sr, sc, dirInfo[d]]
        posInfo[(sr, sc)] = n

    for _ in range(M):
        num, cmd, cnt = list(input().split())
        # (로봇 번호, 명령어(L, R, F), 반복 횟수)
        moveRobot(int(num), cmd, int(cnt))

    print("OK")