#include <iostream>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int N, M, ans;
char A[50][50];
int visit[50][50];

int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,1,-1 };

int bfs(int x, int y) {
    int ret = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            visit[i][j] = -1;
        }
    }
    queue<pair<int, int>> q;
    visit[x][y] = 0;

    q.push({ x,y });
    while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
        for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                if (A[nx][ny] == 'L' && visit[nx][ny] == -1) {
					visit[nx][ny] = visit[x][y] + 1;
					q.push({ nx,ny });
                    ret = max(ret, visit[nx][ny]);
				}
			}
		}
	}

    return ret;
}

int main(void) {
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (A[i][j] == 'L') {
                ans = max(ans, bfs(i, j));
            }
        }
    }
    cout << ans << endl;

    return 0;
}