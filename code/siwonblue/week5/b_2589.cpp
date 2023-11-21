#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int N,M;
vector<vector<int>> map;
vector<vector<int>> visit;
vector<int> dx = {-1,0,1,0};
vector<int> dy = {0,1,0,-1};

void input(){
  cin >> N >> M;
  map.resize(N);
  visit.resize(N, vector<int>(M,0));
  
  for(int i=0;i<N;i++){
    string s;
    cin >> s;
    for(auto c:s) map[i].push_back(c);
  }
  // for(int i=0;i<map.size();i++){
  //   for(int j=0;j<map[i].size();j++){
  //     cout << char(map[i][j]+0) << " ";
  //   }
  //   cout << "\n";
  // }
}

int BFS(int x, int y){
   int cnt=-1;
   int start_x = x, start_y=y;
   for(int i=0;i<N;i++){
    for(int j=0;j<M;j++)
     visit[i][j]=0;
   }

   queue<pair<int,int>> deque;
   deque.push(make_pair(x,y));
   while(!deque.empty()){
    pair<int,int> front = deque.front();
    int x = front.first;
    int y = front.second;
    deque.pop();
    for(int i=0;i<4;i++){
      int nx = x + dx[i];
      int ny = y + dy[i];
      if(nx<0 || ny<0 || nx>=N || ny>=M || char(map[nx][ny]+0)=='W') continue;
      if(visit[nx][ny]) continue;
      if(nx==start_x && ny==start_y) continue;
      cnt = max(visit[x][y]+1,cnt);
      visit[nx][ny] = visit[x][y]+1;
      deque.push(make_pair(nx,ny));
    }
   }
  
  // cout << "\n";
  //  for(int i=0;i<visit.size();i++){
  //     for(int j=0;j<visit[i].size();j++){
  //       cout << visit[i][j] << " ";
  //     }
  //     cout << "\n";
  //  }
  //  cout << "답:"<<cnt;
   return cnt;
}

int solution(){
  int ans = -1;
  input();
  for(int i=0;i<N;i++){
    for(int j=0;j<M;j++){
      if(char(map[i][j]+0)=='W') continue;
      // cout << i<<j<<"에서 최대값:"<< BFS(i,j);
      // cout << "\n";
      ans = max(ans, BFS(i,j));
    }
  }
  return ans;
}

int main(void){
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  freopen("input.txt","r", stdin);
  cout << solution();
}