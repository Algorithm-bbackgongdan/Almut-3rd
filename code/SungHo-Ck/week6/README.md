# Week 6 (1120-1126)
# 30619: 성격 유형 검사하기
- 출처: 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/118666)

## Code
```C++
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(vector<string> servey, vector<int> choices) {
    int mbti[2][4] = { {0,0,0,0},{0,0,0,0} };
    char mbti_char[2][4] = { {'R','C','J','A'},{'T','F','M','N'} };
    string answer = "";
    for (int i = 0; i < servey.size(); i++) {
        if (choices[i] < 4) {
            switch (servey[i][0]) {
            case 'R': mbti[0][0] += 4 - choices[i]; break;
            case 'T': mbti[1][0] += 4 - choices[i]; break;
            case 'C': mbti[0][1] += 4 - choices[i]; break;
            case 'F': mbti[1][1] += 4 - choices[i]; break;
            case 'J': mbti[0][2] += 4 - choices[i]; break;
            case 'M': mbti[1][2] += 4 - choices[i]; break;
            case 'A': mbti[0][3] += 4 - choices[i]; break;
            case 'N': mbti[1][3] += 4 - choices[i];
            }
        }
        else if (choices[i] > 4) {
            switch (servey[i][1]) {
            case 'R': mbti[0][0] += choices[i] - 4; break;
            case 'T': mbti[1][0] += choices[i] - 4; break;
            case 'C': mbti[0][1] += choices[i] - 4; break;
            case 'F': mbti[1][1] += choices[i] - 4; break;
            case 'J': mbti[0][2] += choices[i] - 4; break;
            case 'M': mbti[1][2] += choices[i] - 4; break;
            case 'A': mbti[0][3] += choices[i] - 4; break;
            case 'N': mbti[1][3] += choices[i] - 4;
            }
        }
    }
    for (int i = 0; i < 4; i++) {
        if (mbti[0][i] >= mbti[1][i]) {
            answer.append(1, mbti_char[0][i]);
        }
        else {
            answer.append(1, mbti_char[1][i]);
        }
    }
    return answer;
}
```

## Result
![Alt text](118666.png)
성공

## Access
각 문항에 대한 점수를 배열로 저장한 뒤 최종 배열에 따라 성격 유형을 그대로 출력하였다.




# 30618: 코딩 테스트 공부
- 출처: 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/118668)


## Code
```C++
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
```

## Result
![Alt text](118668.png)
성공

## Access
dp를 이용하여 최소시간을 계산하였다. 모든 문제를 풀수 있는 상태가 필요하기 때문에 현재 수치와 문제의 요구사항들중 최대값을 목적으로 실행한다.

이후 시간 1의 공부를 통한 알고력 혹은 코딩력의 상승과 문제 해결을 통한 상승을 가정하며 dp배열을 채운뒤 최종 시간을 구한다.




# 2589: 등산코스 정하기
- 출처: 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/118669)


## Code
```C++
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
#define INF 987654321

using namespace std;

vector<int> solution(int n, vector<vector<int>> paths, vector<int>gates, vector<int>summits) {
    vector<int> answer = { -1,INF };

    vector<vector<pair<int, int>>> graph(n + 1);
    for (int i = 0; i < paths.size(); i++) {
		graph[paths[i][0]].push_back({ paths[i][1],paths[i][2] });
		graph[paths[i][1]].push_back({ paths[i][0],paths[i][2] });
	}

    vector<int> isSummit(n + 1, 0);
    for (int i = 0; i < summits.size(); i++) {
        isSummit[summits[i]] = 1;
    }

    vector<int> dist(n + 1, INF);
	priority_queue<pair<int, int>> pq;
    for (int i = 0; i < gates.size(); i++) {
		dist[gates[i]] = 0;
		pq.push({ 0,gates[i] });
	}
    while (!pq.empty()) {
		int cur_dist = pq.top().first;
        int cur = pq.top().second;
		pq.pop();
        if (dist[cur] < cur_dist || isSummit[cur]) {
            continue;
        }
        for (int i = 0; i < graph[cur].size(); i++) {
			int next = graph[cur][i].first;
            int next_dist = max(dist[cur], graph[cur][i].second);
            if (dist[next] > next_dist) {
				dist[next] = next_dist;
				pq.push({ next_dist,next });
			}
		}
	}
    for (int i = 0; i < summits.size(); i++) {
        if (answer[1] > dist[summits[i]]) {
			answer[0] = summits[i];
			answer[1] = dist[summits[i]];
		}
        else if (answer[1] == dist[summits[i]]) {
			answer[0] = min(answer[0],summits[i]);
		}
	}
	return answer;
}
```

## Result
![Alt text](image.png)
실패

## Access
출발지에서 산봉우리까지의 최소 intensity의 경로를 구하면 그대로 돌아오면 되므로 편도 경로만을 고려하였다.

다익스트라 알고리즘을 이용하여 출발지부터 산봉우리까지 도달하는 과정에서 intensity가 최소가 되는 경우를 구한다.

마지막 테스트 케이스에서 시간초과가 발생하여 문제를 해결하지 못하였다.