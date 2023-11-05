#include <iostream>
#include <algorithm>
using namespace std;

int price[1001][3];


int main(){
  int N;
  int cost[3];
  cin >> N;
  for(int i=0;i<3;i++) price[0][i] = 0;
  for(int i=1;i<=N;i++){
    cin >> cost[0] >> cost[1] >> cost[2];
    price[i][0] = min(price[i-1][1]+cost[0] , price[i-1][2]+cost[0]);
    price[i][1] = min(price[i-1][0]+cost[1], price[i-1][2]+cost[1]);
    price[i][2] = min(price[i-1][0]+cost[2], price[i-1][1]+cost[2]);
  }
  cout << min(price[N][0], min(price[N][1], price[N][2]));
  return 0;
}