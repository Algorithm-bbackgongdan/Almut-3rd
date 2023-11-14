#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int ans, n, m, r;
int item[101];
int graph[101][101];

int main(void) {
    cin >> n >> m >> r;
    for (int i = 1; i <= n; i++) {
        cin >> item[i];
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i != j)
                graph[i][j] = 16;
        }
    }
    for (int i = 0; i < r; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a][b] = graph[b][a] = c;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                if (graph[j][k] > graph[j][i] + graph[i][k])
                    graph[j][k] = graph[j][i] + graph[i][k];
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        int tmp = 0;
        for (int j = 1; j <= n; j++) {
            if (graph[i][j] <= m)
                tmp += item[j];
        }
        ans = max(ans, tmp);
    }

    cout << ans << endl;

    return 0;
}