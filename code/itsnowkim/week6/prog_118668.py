# 모든 문제들을 풀 수 있는 alp, cop 를 얻는 최단시간은?
def solution(alp, cop, problems):
    # 도달해야 하는 alp, cop
    req_max_alp = max([x[0] for x in problems])
    req_max_cop = max([x[1] for x in problems])
    
    INF = 10e9

    # 이미 목표치보다 커지는 경우 예외 처리
    alp = min(alp, req_max_alp)
    cop = min(cop, req_max_cop)
    

    # 해당 alg, cop 를 얻기까지 소요되는 시간을 저장
    dp = [[INF for _ in range(req_max_cop+1)] for _ in range(req_max_alp+1)]
    
    # init
    dp[alp][cop] = 0
    
    # dp table update
    for i in range(alp, req_max_alp+1):
        for j in range(cop, req_max_cop+1):
            # 알고력 높이기
            # 존재하지 않는 index일 경우 수행 x
            if i+1 <= req_max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)

            # 코딩력 높이기
            if j+1 <= req_max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)

            # 문제 풀기
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                if i>= alp_req and j>=cop_req: # 풀 수 있음
                    # 필요한 범위보다 커지는 경우에 처리
                    ceil_alp,ceil_cop = min(req_max_alp,i + alp_rwd), min(req_max_cop,j + cop_rwd)
                    dp[ceil_alp][ceil_cop] = min(dp[ceil_alp][ceil_cop], dp[i][j]+cost)

    # for d in dp:
        # print(d)
    return dp[-1][-1]

#15
print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))

# 13
print(solution(0,0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))