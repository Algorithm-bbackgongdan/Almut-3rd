#include <iostream>
#include <string>
#include <algorithm>
#define INF 987654321

using namespace std;

long long ans;
int n, e, v1, v2;
long long graph[801][801];

int main(void) {
    cin >> n >> e;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i != j)
                graph[i][j] = INF;
        }
    }

    for (int i = 0; i < e; i++) {
        long long a, b, c;
        cin >> a >> b >> c;
        graph[a][b] = graph[b][a] = c;
    }

    cin >> v1 >> v2;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                if (graph[j][k] > graph[j][i] + graph[i][k])
                    graph[j][k] = graph[j][i] + graph[i][k];
            }
        }
    }

    ans = min(graph[1][v1] + graph[v1][v2] + graph[v2][n], graph[1][v2] + graph[v2][v1] + graph[v1][n]);
    if (ans >= INF)
        cout << -1 << endl;
	else
        cout << ans << endl;

    return 0;
}