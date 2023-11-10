#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

long INF = 2000000000;
int n, m, r;
int items[101];

int main(void) {
  long d[101][101];
  for(int i = 1; i <= 100; i++) {
    for(int j = 1; j <= 100; j++) {
      d[i][j] = d[j][i] = INF;
    }
    d[i][i] = 0;
  }
  
  cin >> n >> m >> r;
  for(int i = 1; i <= n; i++)
    cin >> items[i];
  for(int i = 0; i < r; i++) {
    int a,b,l;
    cin >> a >> b >> l;
    d[a][b] = d[b][a] = l;
  }

  //floyd-warshall
  for(int k = 1; k <= n; k++) {
    for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= n; j++) {
        if (d[i][j] > d[i][k] + d[k][j]) d[i][j] = d[i][k] + d[k][j];
      }
    }
  }

  int res = 0;
  for(int i = 1; i <= n; i++) {
    int cnt = 0;
    for(int j = 1; j <= n; j++) {
      if(d[i][j] <= m) {
        cnt += items[j];
      }
    }
    res = max(res, cnt);
  }
  cout << res << endl;
}