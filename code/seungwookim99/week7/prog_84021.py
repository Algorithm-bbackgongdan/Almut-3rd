from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]

'''
블록 탐색
- search blocks: 블록 조각들 반환
- bfs: 블록 조각 1개 탐색
- out_of_range: bfs 과정 중 좌표 유효성 검사
'''
def search_blocks(board, tile): #(보드, 탐색할 숫자)
    N = len(board)
    visited = [[False]*N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == tile and not visited[i][j]:
                blocks.append(bfs(i, j, board, tile, N, visited))
    return blocks

def bfs(y,x,board,tile, N, visited):
    q = deque([(y,x)])
    block = [(y,x)]
    visited[y][x] = True
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if out_of_range(ny,nx,N) or visited[ny][nx] or board[ny][nx] != tile: continue
            q.append((ny,nx))
            visited[ny][nx] = True
            block.append((ny,nx))
    return block

def out_of_range(y,x,N):
    return (y < 0 or y >= N or x < 0 or x >= N)

'''
블록 전처리 (직사각형으로 감싸기)
- preprocess_blocks: 전처리된 블록 조각들 반환
- preprocess: 블록 조각 1개 전처리
'''
def preprocess_blocks(blocks):
    preprocessed_blocks = []
    for block in blocks:
        preprocessed_blocks.append(preprocess(block))
    return preprocessed_blocks

def preprocess(block):
    min_y, min_x, max_y, max_x = 50, 50, 0, 0
    for y,x in block:
        min_y, min_x = min(min_y, y), min(min_x, x)
        max_y, max_x = max(max_y, y), max(max_x, x)
    N, M = (max_y - min_y + 1), (max_x - min_x + 1) # (높이, 너비)
    preprocessed = [[0]*M for _ in range(N)]
    for y,x in block:
        preprocessed[y-min_y][x-min_x] = 1
    return preprocessed

'''
최대 점수 계산
- compare_blocks: 두 블록 조각 모음을 비교해 최대 점수 반환
- same_matrix_size: 두 블록이 같은 크기의 Matrix로 표현되는지지 비교 (90도 회전시 같아도 same)
- same: 두 블록을 4번 90도 회전시켜 같은지 비교
- rotate: 블록 90도 회전
- compare: 두 블록이 정확히 같은지 비교
- size: 블록의 크기 (1의 개수)
'''
def compare_blocks(A, B):
    answer = 0
    used_A = [False]*len(A)
    used_B = [False]*len(B)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if used_A[i] or used_B[j]: continue # 이미 채워 넣은 조각은 건너 뜀
            if not same_matrix_size(a,b): 
                continue
            if same(a,b): 
                answer += size(a)
                used_A[i] = used_B[j] = True
    return answer

def same_matrix_size(A,B):
    h_A, w_A = len(A), len(A[0])
    h_B, w_B = len(B), len(B[0])
    return (h_A == h_B and w_A == w_B) or (h_A == w_B and w_A == h_B)

def same(A,B):
    h_A, w_A = len(A), len(A[0])
    for _ in range(4):
        B = rotate(B)
        h_B, w_B = len(B), len(B[0])
        if (h_A != h_B) or (w_A != w_B): continue
        if compare(A,B,h_A,w_A):
            return True
    return False

def rotate(block):
    rotated = [list(l) for l in zip(*block[::-1])]
    return rotated

def compare(A,B,H,W):
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]: return False
    return True

def size(block):
    answer = 0
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == 1: answer += 1
    return answer

'''
Main Solution 함수
'''
def solution(game_board, table):    
    # table에서 조각 모으기
    blocks = preprocess_blocks(search_blocks(table, 1))
    
    # game_board에서 빈 조각 모으기
    emptys = preprocess_blocks(search_blocks(game_board, 0))

    # 비교하기    
    return compare_blocks(blocks,emptys)