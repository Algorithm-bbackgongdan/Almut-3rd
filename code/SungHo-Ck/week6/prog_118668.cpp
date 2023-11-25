#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#define INF 987654321

using namespace std;

int solution(int alp, int cop, vector<vector<int>> problems) {
    int answer = 0;
    int alp_need = alp;
    int cop_need = cop;
    for (int i = 0; i < problems.size(); i++) {
        alp_need = max(alp_need, problems[i][0]);
        cop_need = max(cop_need, problems[i][1]);
    }
    vector<vector<int>>dp(alp_need + 1, vector<int>(cop_need + 1, INF));
    
    alp = min(alp, alp_need);
    cop = min(cop, cop_need);
    dp[alp][cop] = 0;

    for (int i = alp; i <= alp_need; i++) {
        for (int j = cop; j <= cop_need; j++) {
            if (i < alp_need) {
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1);
            }
            if (j < cop_need) {
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1);
            }
            for (int k = 0; k < problems.size(); k++) {
                if (i >= problems[k][0] && j >= problems[k][1]) {
                    int tmp_a = min(i + problems[k][2], alp_need);
                    int tmp_c = min(j + problems[k][3], cop_need);
                    dp[tmp_a][tmp_c] = min(dp[tmp_a][tmp_c], dp[i][j] + problems[k][4]);
                }
            }
        }
    }

    return dp[alp_need][cop_need];
}

int main(void) {
    vector<vector<int>> problems = { {10,15,2,1,2} ,{20,20,3,3,4} };
    int ans = solution(10,10, problems);
    cout << ans << endl;

    problems = { {0,0,2,1,2} ,{4,5,3,1,2},{4,11,4,0,2},{10,4,0,4,2} };
    ans = solution(0,0, problems);
    cout << ans << endl;
    return 0;
}