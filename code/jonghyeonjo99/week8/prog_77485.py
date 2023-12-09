def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1

    for start_x, start_y, end_x, end_y in queries:
        min_num = arr[start_x-1][start_y-1]

        #위쪽 테두리
        for i in range(end_y-1,start_y,-1):
            arr[start_x-1][i] = arr[start_x-1][i-1]
            min_num = min(min_num, arr[start_x-1][i])

        #우측 테두리
        for i in range(end_x-1,start_x,-1):
            arr[i][end_y-1] = arr[i-1][end_y-1]
            min_num = min(min_num, arr[i][end_y-1])

        #아래 테두리
        for i in range(start_y,end_y):
            arr[end_x-1][i-1] = arr[end_x-1][i]
            min_num = min(min_num, arr[end_x-1][i])

        #좌측 테두리
        for i in range(start_x,end_x):
            arr[i-1][start_y-1] = arr[i][start_y-1]
            min_num = min(min_num, arr[i][start_y-1])

        answer.append(min_num)
    return answer