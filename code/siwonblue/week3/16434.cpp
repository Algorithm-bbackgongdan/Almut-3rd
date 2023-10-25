#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

struct Me{
  long long cur;
  long long max;
  long long attack;
};

bool train(Me me, vector<vector<long long>> room_info){
  
  bool killDragon = true;
  for(long long i=0;i<room_info.size();i++){
    vector<long long> room = room_info[i];
    long long type = room[0];
    if(type==2){
      me.attack += room[1];
      me.cur += room[2];
      if(me.cur>=me.max) me.cur = me.max;
      continue;
    }
    while(true){
      room[2] -= me.attack;
      if(room[2]<=0) break;
      
      me.cur -= room[1];
      if(me.cur<=0){
        killDragon = false;
        return killDragon;
      }
    }
  }
  
  return killDragon;
}

int main(){
  // input
  long long N, attack;
  cin >> N >> attack;
  vector<vector<long long>> room_info(N, vector<long long>(3, 0));
  
  for(long long i=0;i<N;i++){
    long long type, a,b;
    cin >> type >> a >> b;
    room_info[i] = vector<long long>{type,a,b};
  };

  long long maxHp = pow(10,7)  * 123456;

  long long start = 1;
  long long end = maxHp;
  long long ans = maxHp+1;
  while(start<=end){
    long long mid = (start+end)/2;
     Me me = {mid, mid, attack};
     
     bool killDragon;
     killDragon = train(me, room_info);
    
     if(killDragon){  
      ans = min(ans, mid);
      end = mid - 1;
     }else{
      start = mid + 1;
     };
  };
  
  cout << ans;
  
  return 0;
}