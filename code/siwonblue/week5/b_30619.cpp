#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int N,M,L,R;
vector<int> houses;

void operation(){
  cin >> L >> R;
  vector<int> copy = houses;
  for(int i=0;i<copy.size();i++){
    if(copy[i]>max(L,R) || copy[i]<min(L,R)) continue;
    for(int j=i+1;j<copy.size();j++){
      if(copy[j]>max(L,R) || copy[j]<min(L,R)) continue;
      if(copy[i] > copy[j]) swap(copy[i],copy[j]);
    }
  }
  for(auto c:copy) cout << c << " ";
  cout << "\n";
}

void input(){
  cin >> N;
  houses.resize(N);
  for(int i=0;i<N;i++)
    cin >> houses[i];
  cin >> M;
  // O() : 2.7 * 10^7
  for(int i=0;i<M;i++){
    operation();
  }
}

void solution(){
  input();
}

int main(void){
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  freopen("input.txt","r", stdin);
  solution();
}