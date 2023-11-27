function solution(alp, cop, problems) {
    var answer = 0;
    let [maxAlp, maxCop] = [0, 0];

    problems.forEach(([alp_req, cop_req]) => {
        maxAlp = Math.max(maxAlp, alp_req);
        maxCop = Math.max(maxCop, cop_req);
    });

    const dp = new Array(maxAlp + 1)
        .fill()
        .map(() => new Array(maxCop + 1).fill(Number.MAX_SAFE_INTEGER));

    alp = Math.min(alp, maxAlp);
    cop = Math.min(cop, maxCop);

    dp[alp][cop] = 0;

    for (let i = alp; i <= maxAlp; i++) {
        for (let j = cop; j <= maxCop; j++) {
            // 알고리즘 공부
            if (i + 1 <= maxAlp) {
                dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
            }
            // 코딩 공부
            if (j + 1 <= maxCop) {
                dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);
            }
            // 문제 풀기
            problems.forEach(([alp_req, cop_req, alp_rwd, cop_rwd, cost]) => {
                if (i >= alp_req && j >= cop_req) {
                    const nextAlp = Math.min(i + alp_rwd, maxAlp);
                    const nextCop = Math.min(j + cop_rwd, maxCop);

                    dp[nextAlp][nextCop] = Math.min(
                        dp[nextAlp][nextCop],
                        dp[i][j] + cost
                    );
                }
            });
        }
    }

    answer = dp[maxAlp][maxCop];

    return answer;
}
