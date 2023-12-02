#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 };

vector<vector<int>> rotate(vector<vector<int>> puzzle) {
	vector<vector<int>> ret;
	int n = puzzle.size();
    for (int i = 0; i < n; i++) {
		vector<int> tmp;
        for (int j = n - 1; j >= 0; j--) {
			tmp.push_back(puzzle[j][i]);
		}
		ret.push_back(tmp);
	}
	return ret;
}

vector<vector<int>> getEmptyBoard(vector<vector<int>> game_board) {
	vector<vector<int>> ret;
	int n = game_board.size();
    for (int i = 0; i < n; i++) {
		vector<int> tmp;
        for (int j = 0; j < n; j++) {
            if (game_board[i][j] == 0) {
				tmp.push_back(1);
			}
            else {
				tmp.push_back(0);
			}
		}
		ret.push_back(tmp);
	}
	return ret;
}

vector<vector<pair<int, int>>> find(vector<vector<int>> game_board, int key) {
	vector<vector<pair<int,int>>> ret;
	vector<vector<bool>> visit = vector<vector<bool>>(game_board.size(), vector<bool>(game_board[0].size(), false));
	int n = game_board.size();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visit[i][j] && game_board[i][j] == key) {
				queue<pair<int, int>> q;
				q.push({ i, j });
				game_board[i][j] = key ^ 1;
				visit[i][j] = true;
				queue<pair<int, int>> lst;
				lst.push({ i, j });

				while (!q.empty()) {
					int x = q.front().first;
					int y = q.front().second;
					q.pop();
					for (int k = 0; k < 4; k++) {
						int nx = x + dx[k];
						int ny = y + dy[k];
						if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
						if (visit[nx][ny] || game_board[nx][ny] != key) continue;
						visit[nx][ny] = true;
						q.push({ nx, ny });
						lst.push({ nx, ny });
					}
				}
				vector<pair<int, int>> tmp;
				while (lst.empty()) {
					tmp.push_back({ lst.front().first, lst.front().second });
					lst.pop();
				}
				ret.push_back(tmp);
			}
		}
	}
	return ret;
}

int solution(vector<vector<int>> game_board, vector<vector<int>> table) {
    int answer = 0;
	vector<vector<pair<int, int>>> emptyBoard = find(game_board, 0);
	vector<vector<pair<int, int>>> puzzle = find(table, 1);

	int n = game_board.size();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << "(" << emptyBoard[i][j].first << " " << emptyBoard[i][j].second << ")";
		}
		cout << endl;
	}

    return answer;
}

int main(void) {
    vector<vector<int>> game_board = {{1, 1, 0, 0, 1, 0}, {0, 0, 1, 0, 1, 0}, {0, 1, 1, 0, 0, 1}, {1, 1, 0, 1, 1, 1}, {1, 0, 0, 0, 1, 0}, {0, 1, 1, 1, 0, 0}};
    vector<vector<int>> table = {{1, 0, 0, 1, 1, 0}, {1, 0, 1, 0, 1, 0}, {0, 1, 1, 0, 1, 1}, {0, 0, 1, 0, 0, 0}, {1, 1, 0, 1, 1, 0}, {0, 1, 0, 0, 0, 0}};
    int ans = solution(game_board, table);
    cout << ans << endl;

    game_board = { {0, 0, 0},{1, 1, 0},{1, 1, 1} };
    table = {{1, 1, 1}, {1, 0, 0}, {0, 0, 0}};
    ans = solution(game_board, table);
    cout << ans << endl;

    return 0;
}