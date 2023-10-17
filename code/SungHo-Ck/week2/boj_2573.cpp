//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

int N,M;
int arr[300][300];
int visit[300][300];
int melt[300][300];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

bool isICE() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (arr[i][j] > 0)
                return true;
        }
    }
    return false;
}

void dfs(int x, int y) {
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || ny < 0 || nx >= N || ny >= M)
            continue;
        if (arr[nx][ny] > 0 && visit[nx][ny] == 0) {
            visit[nx][ny] = 1;
            dfs(nx, ny);
        }
    }
}

int main(void) {
    int i, j, answer;

    std::cin >> N >> M;
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            std::cin >> arr[i][j];
        }
    }

    answer = 0;
    while (1) {
        for (i = 0; i < N; i++) {
            for (j = 0; j < M; j++) {
                visit[i][j] = 0;
                melt[i][j] = 0;
            }
        }

        // No Ice
        if (!isICE()) {
            std::cout << "0";
            break;
        }

        // calc Ice cnt
        int cnt = 0;
        for (i = 0; i < N; i++) {
            for (j = 0; j < M; j++) {
                if (arr[i][j] > 0 && visit[i][j] == 0) {
					visit[i][j] = 1;
                    cnt++;
					dfs(i, j);
				}
			}
		}
        if (cnt > 1) {
            std::cout << answer;
            break;
        }
        else
            answer++;

        // calc Melt
        for (i = 0; i < N; i++) {
            for (j = 0; j < M; j++) {
                if (arr[i][j] > 0) {
                    for (int k = 0; k < 4; k++) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if (nx < 0 || ny < 0 || nx >= N || ny >= M)
                            continue;
                        if (arr[nx][ny] <= 0)
                            melt[i][j]++;
                    }
				}
			}
		}

        for (i = 0; i < N; i++) {
            for (j = 0; j < M; j++) {
                arr[i][j] -= melt[i][j];
            }
        }
    }
    return 0;
}