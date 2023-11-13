def solution(board, skill):
    n, m = len(board), len(board[0])

    # 건물 내구도
    durability = [[0] * m for _ in range(n)]

    # 초기 내구도 할당
    for i in range(n):
        for j in range(m):
            durability[i][j] = board[i][j]

    # 스킬 적용
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if type == 1:
                    durability[i][j] -= degree
                elif type == 2:
                    durability[i][j] += degree

    # 최종 내구도 계산
    count = 0
    for i in range(n):
        for j in range(m):
            if durability[i][j] > 0:
                count += 1

    return count
