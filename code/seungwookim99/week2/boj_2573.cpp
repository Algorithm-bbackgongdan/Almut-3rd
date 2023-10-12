// C++ 풀이
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <tuple>

#define MAX 301

using namespace std;

int dy[4] = {0,1,0,-1};
int dx[4] = {1,0,-1,0};

int N, M;
int board[MAX][MAX];
int year = 0;

struct Point {
  int y, x, num;
};

bool out_of_range_(int y, int x) {
  return (0 > y) || (0 > x) || (N <= y) || (M <= x);
}

void bfs(int y, int x, int glacier[MAX][MAX], int num) {
  queue<Point> q;
  Point start;
  start.y = y, start.x = x;
  q.push(start);
  while (!q.empty()) {
    Point curr = q.front();
    q.pop();
    for (int i = 0 ; i < 4 ; i++) {
      int ny = curr.y + dy[i];
      int nx = curr.x + dx[i];
      if (out_of_range_(ny,nx)) continue;
      if ((board[ny][nx] > 0) && (glacier[ny][nx] == 0)) {
        glacier[ny][nx] = num;
        Point next;
        next.y = ny, next.x = nx;
        q.push(next);
      }
    }
  }
}

int count_glacier() {
  int cnt = 0;
  int glacier[MAX][MAX] = {0,};
  for (int i = 0 ; i < N ; i++) {
    for (int j = 0 ; j < M ; j++) {
      if (board[i][j] == 0) continue; // 바닷물 skip
      if (cnt == 0) bfs(i, j, glacier, ++cnt); // 최초 빙하 덩어리 1로 매핑
      else if (glacier[i][j] == cnt) continue; // 1번 빙하 skip
      else return ++cnt; // 1번이 아닌 다른 빙하 조각 발견
    }
  }
  return cnt;
}

void melt() {
  vector<Point> candidate;
  for (int i = 0 ; i < N ; i++) {
    for (int j = 0 ; j < M ; j++) {
      if (board[i][j] == 0) continue;
      int cnt = 0;
      for (int k = 0 ; k < 4 ; k++) {
        int ny = i + dy[k], nx = j + dx[k];
        if (board[ny][nx] == 0) cnt++;
      }
      if (cnt > 0) {
        Point p;
        p.y = i, p.x = j, p.num = cnt;
        candidate.push_back(p); // 녹을 빙하 좌표, offset 저장
      }
    }
  }
  for (int i = 0 ; i < candidate.size() ; i++) {
    Point p = candidate[i];
    if (board[p.y][p.x] < p.num) board[p.y][p.x] = 0;
    else board[p.y][p.x] -= p.num; // 녹이기
  }
}

int main(void) {
  cin >> N >> M;
  for (int i = 0 ; i < N ; i ++) {
    for (int j = 0 ; j < M ; j++) {
      cin >> board[i][j];
    }
  }
  while(true) {
    /* 빙산 개수 count */
    int cnt = count_glacier();
    if (cnt == 0) {
      year = 0;
      break;
    }
    else if (cnt > 1) break;

    /* 빙산 녹임 */
    melt();
    year++;
  }
  cout << year << endl;
  return 0;
}