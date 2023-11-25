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
    sort(summits.begin(), summits.end());
    for (int i = 0; i < summits.size(); i++) {
        if (answer[1] > dist[summits[i]]) {
			answer[0] = summits[i];
			answer[1] = dist[summits[i]];
		}
	}
	return answer;
}

int main(void) {
    vector<vector<int>> paths = { {1, 2, 3} ,{2, 3, 5},{2, 4, 2},{2, 5, 4},{3, 4, 4},{4, 5, 3},{4, 6, 1},{5, 6, 1} };
    vector<int> gates = { 1,3 };
    vector<int> summits = { 5 };
    vector<int> ans = solution(6, paths, gates, summits);
    cout << ans[0] << "," << ans[1] << endl;

    paths = { {1, 4, 4} ,{1, 6, 1},{1, 7, 3},{2, 5, 2},{3, 7, 4},{5, 6, 6} };
    gates = { 1 };
    summits = { 2,3,4 };
    ans = solution(7, paths, gates, summits);
    cout << ans[0] << "," << ans[1] << endl;

    paths = { {1, 2, 5} ,{1, 4, 1},{2, 3, 1},{2, 6, 7},{4, 5, 1},{5, 6, 1},{6, 7, 1} };
    gates = { 3,7 };
    summits = { 1,5 };
    ans = solution(7, paths, gates, summits);
    cout << ans[0] << "," << ans[1] << endl;

    paths = { {1, 3, 10} ,{1, 4, 20},{2, 3, 4},{2, 4, 6},{3, 5, 20},{4, 5, 6} };
    gates = { 1,2 };
    summits = { 5 };
    ans = solution(5, paths, gates, summits);
    cout << ans[0] << "," << ans[1] << endl;
    return 0;
}