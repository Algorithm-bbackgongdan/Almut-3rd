#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

int N,E,v1,v2;
int INF = 1e9;
vector<vector<pair<int,int>>> maps;
vector<int> dist;


void input(){
  cin >> N >> E;
  maps.resize(N+1);
  dist.resize(N+1, INF);
  for(int i=0;i<E;i++){
    int start, end, dis;
    cin >> start >> end >> dis;
    maps[start].push_back(make_pair(end,dis));
    maps[end].push_back(make_pair(start,dis));
  }
  cin >> v1 >> v2;
  // for(int i=1;i<maps.size();i++){
  //   cout << i <<"에 연결된 점";
  //   for(int j=0;j<maps[i].size();j++){
  //     cout << maps[i][j].first << " ";
  //   }
  //   cout<<"\n";
  // }
}

void dijkstra(int start){
  priority_queue<pair<int,int>> pq;
  pq.push(make_pair(0,start));
  for(int i=0;i<dist.size();i++) dist[i] = INF;
  dist[start] = 0;
  while(!pq.empty()){
    int cost = -pq.top().first;
    int cur_node = pq.top().second;
    pq.pop();
    for(int i=0;i<maps[cur_node].size();i++){
      int next = maps[cur_node][i].first;
      int next_cost = maps[cur_node][i].second;
      if(dist[next] > cost + next_cost){
        dist[next] = cost + next_cost;
        pq.push(make_pair(-dist[next], next));
      }
    }
  }
  // for(int i=1;i<dist.size();i++) cout << dist[i] << " ";
  // cout << "\n";
}

void solution(){
  int ans = INF;
  input();

  dijkstra(1);
  int oneToV1 = dist[v1];
  int oneToV2 = dist[v2];
  
  dijkstra(v1);
  int v1ToV2 = dist[v2];
  int v1ToN = dist[N];

  dijkstra(v2);
  int v2ToN = dist[N];

	ans = min(ans, oneToV1 + v1ToV2 + v2ToN);
	ans = min(ans, oneToV2 + v1ToV2 + v1ToN);
	if (v1ToV2 == INF || ans == INF) cout << -1;
	else cout << ans;
  
}

int main(void){
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  // freopen("input.txt", "r", stdin);
  solution();
}
