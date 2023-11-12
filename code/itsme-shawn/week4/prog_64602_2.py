def solution(board, skill):
    answer = 0

    n, m = len(board), len(board[0])

    # 누적합을 저장하는 2차원 배열
    temp = [[0] * (m + 1) for _ in range(n + 1)]

    # 스킬 적용
    # 누적합을 기록
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        if type == 1:
            temp[r1][c1] -= degree
            temp[r1][c2 + 1] += degree
            temp[r2 + 1][c1] += degree
            temp[r2 + 1][c2 + 1] -= degree
        elif type == 2:
            temp[r1][c1] += degree
            temp[r1][c2 + 1] -= degree
            temp[r2 + 1][c1] -= degree
            temp[r2 + 1][c2 + 1] += degree

    # 최종 누적합 계산

    # 행 기준 누적합
    for i in range(n):
        for j in range(m):
            temp[i][j + 1] += temp[i][j]

    # 열 기준 누적합
    for j in range(m):
        for i in range(n):
            temp[i + 1][j] += temp[i][j]

    # 기존 배열과 합함
    for i in range(n):
        for j in range(m):
            board[i][j] += temp[i][j]

            # board에 값이 1이상인 경우 answer 증가
            if board[i][j] > 0:
                answer += 1

    return answer
