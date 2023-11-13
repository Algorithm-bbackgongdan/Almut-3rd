#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

vector<vector<pair<int,int>>> maps;
vector<int> dist;
vector<int> items;
int n,m,r;
int INF = 1e9;

void input(){
  cin >> n >> m >> r;
  maps.resize(n+1);
  items.resize(n+1,0);
  dist.resize(n+1, INF);
  for(int i=1;i<=n;i++){
    int item;
    cin >> item;
    items[i] = item;
  }
  // for(int i=1;i<items.size();i++) cout << items[i];
  for(int i=0;i<r;i++){
    int start, end, dis;
    cin >> start >> end >> dis;
    maps[start].push_back(make_pair(end,dis));
    maps[end].push_back(make_pair(start,dis));
  }

  // for(int i=1;i<maps.size();i++){
  //   cout << i << "에 연결된 점";
  //   for(int j=0;j<maps[i].size();j++){
  //     cout << maps[i][j].first  << " ";
  //   }
  //   cout << "\n";
  // }
}

int dijkstra(int v){
  int sum = 0;
  priority_queue<pair<int,int>> pq;
  pq.push(make_pair(0,v));
  for(int i=0;i < dist.size();i++) dist[i]=INF;
  dist[v] = 0;
  while(!pq.empty()){
    int cost = -pq.top().first;
    int cur = pq.top().second;
    pq.pop();
    for(int i=0;i<maps[cur].size();i++){
      int end = maps[cur][i].first;
      int nCost = maps[cur][i].second;
      if(dist[end] > cost + nCost){
        dist[end] = cost + nCost;
        pq.push(make_pair(-dist[end], end));
      }
    }
  }
  for(int i=1;i<dist.size();i++){
    if(dist[i] <= m) sum += items[i];
  };
  // cout << v << "에서의 수색 값은 :" << sum << "\n";
  return sum;
}

void solution(){
  int ans=0;
  input();
  for(int i=1;i<=n;i++){
    ans = max(dijkstra(i),ans);
  }
  cout << ans;
}

int main(void){
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  // freopen("input.txt", "r", stdin);
  solution();
}
