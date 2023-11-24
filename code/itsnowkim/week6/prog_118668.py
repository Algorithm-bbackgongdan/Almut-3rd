# 모든 문제들을 풀 수 있는 alp, cop 를 얻는 최단시간은?
def safe_index(i,j):
    return 0<=i and 0<=j
def solution(alp, cop, problems):
    answer = 0

    # 도달해야 하는 alp, cop
    req_max_alp = max([x[0] for x in problems])
    req_max_cop = max([x[1] for x in problems])
    
    INF = 10e9

    # 해당 alg, cop 를 얻기까지 소요되는 시간을 저장
    dp = [[INF for _ in range(req_max_cop+1)] for _ in range(req_max_alp+1)]
    
    # 초기 주어진 값보다 작거나 같은 경우, 걸리는 시간은 0
    for i in range(alp+1):
        for j in range(cop+1):
            dp[i][j] = 0
    
    # dp table update
    for i in range(req_max_alp+1):
        for j in range(req_max_cop+1):
            # 알고력 높이기
            # 존재하지 않는 index일 경우 수행 x
            if safe_index(i-1, j):
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j])

            # 코딩력 높이기
            if safe_index(i, j-1):
                dp[i][j] = min(dp[i][j-1] + 1, dp[i][j])

            # 문제 풀기
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                if i>= alp_req and j>=cop_req: # 풀 수 있음
                    if safe_index(i-alp_rwd, j-cop_rwd):
                        dp[i][j] = min(dp[i][j], dp[i-alp_rwd][j-cop_rwd] + cost)

    # for d in dp:
    #     print(d)
    return dp[req_max_alp][req_max_cop]

#15
print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))

# 13
print(solution(0,0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))