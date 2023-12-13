def solution(rows, columns, queries):
    answer = []
    board = []
    # 행렬 초기화
    for row in range(rows):
        tmp = []
        for col in range(columns):
            tmp.append(row * columns + col + 1)
        board.append(tmp)
        
    for x1,y1,x2,y2 in queries:
        x1 -=1
        y1 -=1
        x2 -=1
        y2 -=1
        min_num = initial_value = board[x1][y1]
        # 좌측 테두리 갱신
        for i in range(x1,x2):
            board[i][y1] = board[i+1][y1]
            min_num = min(min_num, board[i][y1])
        # 하단 테두리 갱신
        for i in range(y1,y2):
            board[x2][i] = board[x2][i+1]
            min_num = min(min_num, board[x2][i])
        # 우측 테두리 갱신
        for i in range(x2,x1,-1):
            board[i][y2] = board[i-1][y2]
            min_num = min(min_num, board[i][y2])
        # 상단 테두리 갱신
        for i in range(y2,y1,-1):
            board[x1][i] = board[x1][i-1]
            min_num = min(min_num, board[x1][i])
        board[x1][y1+1] = initial_value
        answer.append(min_num)
    return answer