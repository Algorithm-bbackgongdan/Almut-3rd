#include <iostream>
#include <queue>
#include <vector>

using namespace std;

long INF = 1000000000;

int N, E, u, v;
long d[801];
vector<pair<int,long> > edges[801];

void dijkstra(int start) {
  for(int i = 0; i < 801; i++)
    d[i] = INF;
  d[start] = 0;
  priority_queue<pair<long, int> > pq;
  pq.push(make_pair(0, start));
  while(!pq.empty()) {
    int curr = pq.top().second;
    long distance = -pq.top().first;
    pq.pop();
    if(d[curr] < distance) continue;
    for(int i = 0; i < edges[curr].size(); i++) {
      int next = edges[curr][i].first;
      long newDistance = distance + edges[curr][i].second;
      if (newDistance < d[next]) {
        d[next] = newDistance;
        pq.push(make_pair(-newDistance, next));
      }
    }
  }
}

int main(void) {
  cin >> N >> E;
  for(int i = 0; i < E; i++) {
    int a,b;
    long c;
    cin >> a >> b >> c;
    edges[a].push_back(make_pair(b,c));
    edges[b].push_back(make_pair(a,c));
  }
  cin >> u >> v;
  // from 1
  dijkstra(1);
  long oneToU = d[u], oneToV = d[v];

  // from u
  dijkstra(u);
  long uToV = d[v], uToN = d[N];

  // from v
  dijkstra(v);
  long vToU = d[u], vToN = d[N];

  long res = min(oneToU + uToV + vToN, oneToV + vToU + uToN);
  if (res >= INF) res = -1;
  cout << res << endl;
  return 0;
}