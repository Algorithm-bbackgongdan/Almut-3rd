def calculation(n, m, skill_list):
    matrix = [[0]*(m) for _ in range((n))]
    
    for skill in skill_list:
        skill_type, s1, s2, e1, e2, pow = skill
        
        # skill type 에 따라 행동 분기
        if skill_type == 1:
            matrix[s1][s2] -= pow
            matrix[s1][e2+1] += pow
            matrix[e1+1][s2] += pow
            matrix[e1+1][e2+1] -= pow
        else:
            matrix[s1][s2] += pow
            matrix[s1][e2+1] -= pow
            matrix[e1+1][s2] -= pow
            matrix[e1+1][e2+1] += pow
    
    return matrix

def solution(board, skill):
    answer = 0

    # skill 에 따라 행렬 합 구하기
    N = len(board)
    M = len(board[0])
    
    matrix = calculation(N+1, M+1, skill)

    # matrix update
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            matrix[i][j+1] += matrix[i][j]

    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            matrix[i+1][j] += matrix[i][j]


    # board update
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += matrix[i][j]
            if board[i][j] >0:
                answer+=1
    
    return answer


# ans : 10
# solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
# ans : 6
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))

# 11 22 4
# 00 11 2

# -2 -2 0
# -2 -6 -4
# 100 -4 -4

[-2, 0, 2, 0]
[0, -4, 0, 4]
[102, -100, 2, 0]
[-100, -96, 0, 4]

[-2, -2, 0]
[-2, -6, 0]
[100, -4, 4]
