def solution(alp, cop, problems):
    INF = int(1e12)
    answer = INF
    MAX_ALP = max([prob[0] for prob in problems])
    MAX_COP = max([prob[1] for prob in problems])
    
    # init dp matrix (alp x cop)
    dp = [[INF] * 181 for _ in range(181)]
    dp[alp][cop] = 0 # base case
    for i in range(alp, MAX_ALP+1):
        for j in range(cop, MAX_COP+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_rwd: continue
                dp[i+alp_rwd][j+cop_rwd] = min(dp[i][j] + cost, dp[i+alp_rwd][j+cop_rwd])
    return dp[MAX_ALP][MAX_COP]