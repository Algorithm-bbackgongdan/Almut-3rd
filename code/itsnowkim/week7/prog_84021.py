from collections import deque

"""
matrix 돌리는 함수
"""
def rotate(mat):
    n = len(mat)
    m = len(mat[0])

    # n*m -> m*n
    res = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            res[i][j] = mat[n-j-1][i]

    return res

"""
두 matrix 가 fit 한지 체크
"""
def summation_check(mat1, mat2):
    # 가로, 세로 길이가 일단 맞아야됨
    n = len(mat1)
    m = len(mat1[0])
    
    if len(mat1)==len(mat2) and len(mat1[0]) == len(mat2[0]):
        for i in range(n):
            for j in range(m):
                if mat1[i][j] + mat2[i][j] != 1:
                    return False
        return True
    return False

"""
matrix 의 1 개수 세는 함수
"""
def count(mat):
    ans = 0
    for m in mat:
        ans += sum(m)
    return ans

"""
N*M 직사각형 크기로 matrix 를 복사하고 return 하는 함수
"""
def make_piece(target, board, N):
    minx, miny = N, N
    maxx, maxy = 0, 0
    INIT = board[target[0][0]][target[0][1]]
    VAL = 0
    if INIT == 1:
        INIT = 0
        VAL = 1
    else:
        INIT = 1
        VAL = 0
    
    for x, y in target:
        if x < minx:
            minx = x
        elif x > maxx:
            maxx = x

        if y < miny:
            miny = y
        elif y > maxy:
            maxy = y
    
    x = (maxx-minx+1)
    y = (maxy-miny+1)

    # 빈 값으로 초기화
    temp = [[INIT]*max(y,1) for _ in range(max(x,1))]

    # target 을 순회하며 값을 넣기
    for tx, ty in target:
        i = tx-minx
        j = ty-miny
        temp[i][j] = VAL

    # board 복사
    # for idxi, i in enumerate(range(minx, maxx+1)):
    #     for idxj, j in enumerate(range(miny, maxy+1)):
    #         temp[idxi][idxj] = board[i][j]
    return temp

"""
1. table 에 있는 block 의 시작점을 저장하기
2. game_board 에 넣을 수 있는 칸을 순회하기
3. 빈 칸을 마주하면, table 의 block 과 fit 한 block 이 있는지 체크
fit 할 경우 - count 증가
fit 하지 않을 경우 - pass
*fit 한 조건을 찾는 방법 : 회전 총 4번 시키기
"""
def solution(game_board, table):
    answer = 0
    direction = [(-1,0), (0,-1), (0,1), (1,0)]

    # 1. table 에 있는 block 의 시작점을 저장하기 - block 의 x,y 의 min, max 저장
    blocks = []
    N = len(table)
    visited = [[False]*N for _  in range(N)]
    for i in range(N):
        for j in range(N):
            # 블록!
            if table[i][j] == 1 and not visited[i][j]:
                block = []
                q = deque([(i,j)])

                while q:
                    curr_i, curr_j = q.popleft()
                    visited[curr_i][curr_j] = True
                    block.append((curr_i, curr_j))

                    for x, y in direction:
                        next_i = curr_i + x
                        next_j = curr_j + y

                        # board 안에 있으면서 block 일 경우
                        if 0<=next_i and next_i<N and 0<=next_j and next_j<N and table[next_i][next_j]==1 and not visited[next_i][next_j]:
                            q.append((next_i, next_j))
                
                # block 에 i, j 저장 완료
                blocks.append(make_piece(block, table, N))

    # space 에 맞는 조각이 있으면 return true
    def check(space):
        res = 0
        
        for b in blocks:
            if summation_check(space, b):
                res = count(b)
                blocks.remove(b)
                break
            if summation_check(space, rotate(b)):
                res = count(b)
                blocks.remove(b)
                break
            if summation_check(space, rotate(rotate(b))):
                res = count(b)
                blocks.remove(b)
                break
            if summation_check(space, rotate(rotate(rotate(b)))):
                res = count(b)
                blocks.remove(b)
                break
        return res

    # 2. game_board 에 넣을 수 있는 칸을 순회하기
    visited = [[False]*N for _  in range(N)]
    for i in range(N):
        for j in range(N):
            # 3. 빈 칸을 마주하면, table 의 block 과 fit 한 block 이 있는지 체크, 먼저 빈 칸의 모양을 확인
            if game_board[i][j] == 0 and not visited[i][j]:
                space = []
                q = deque([(i,j)])

                while q:
                    curr_i, curr_j = q.popleft()
                    visited[curr_i][curr_j] = True
                    space.append((curr_i, curr_j))

                    for x, y in direction:
                        next_i = curr_i + x
                        next_j = curr_j + y

                        # board 안에 있으면서 block 일 경우
                        if 0<=next_i and next_i<N and 0<=next_j and next_j<N and game_board[next_i][next_j]==0 and not visited[next_i][next_j]:
                            q.append((next_i, next_j))
                
                # space 에 i, j 저장 완료, check 함수로 보내서 check
                temp = make_piece(space, game_board, N)
                answer += check(temp)

    return answer


# 14
# print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
# 0
# print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]	))
# 6
# print(solution([[1, 0, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 1, 1], [1, 0, 1]]))
# 54
print(solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],[[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]))