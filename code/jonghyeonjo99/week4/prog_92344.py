def solution(board, skill):
    answer = 0
    imos = [[0 for _ in range(len(board[1]) + 1)] for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            imos[r1][c1] -= degree
            imos[r2 + 1][c1] += degree
            imos[r1][c2 + 1] += degree
            imos[r2 + 1][c2 + 1] -= degree
        else: #type == 2
            imos[r1][c1] += degree
            imos[r2 + 1][c1] -= degree
            imos[r1][c2 + 1] -= degree
            imos[r2 + 1][c2 + 1] += degree
    
    #누적합 두번
    for i in range(len(board) + 1):
        for j in range(1,len(board[1]) + 1):
            imos[i][j] += imos[i][j-1]
    
    for j in range(len(board[1]) + 1):
        for i in range(1,len(board) + 1):
            imos[i][j] += imos[i-1][j]
    
    #board에 적용
    for i in range(len(board)):
        for j in range(len(board[1])):
            board[i][j] += imos[i][j]
            if board[i][j] > 0:
                answer += 1
            
    return answer