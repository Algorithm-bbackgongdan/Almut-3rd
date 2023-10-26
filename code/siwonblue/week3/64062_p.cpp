#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> cross_bridge(vector<int> stones,int mid){
  vector<int> deep_copy_stones = stones; 
  for(int i=0;i<deep_copy_stones.size();i++){
    deep_copy_stones[i] = deep_copy_stones[i] - mid <0 ? 0 : deep_copy_stones[i] - mid ;
  };
  return deep_copy_stones;
};

int check(vector<int> stones, int k){
  int sum = 0; // 2* 10**8 * 2 * 10**5 
  int cnt = 0;
  
  for(int i=0;i<k;i++) sum+=stones[i];
  if(sum==0) cnt+=1;
  for(int i=k;i<stones.size();i++){
    sum += stones[i] - stones[i-k];
    if(sum==0) cnt+=1;
  };
  if (cnt<1)  return 0;
  if (cnt==1) return 1;
  else return 2;
};


int search(vector<int> stones, int high, int k){
  int start = 1;
  int end = high;
  int ans = -1;
  int cnt;
  vector<int> deep_copy_stones;
  while(start<=end){
    int mid = (start+end)/2;
    
    deep_copy_stones = cross_bridge(stones,mid);
    // cout << "start:" << start<<" ";
    // cout << "end:" << end<<" ";
    // cout << "mid:" << mid <<" "<< "\n";

    // for(int i=0;i<deep_copy_stones.size();i++) cout << deep_copy_stones[i] << " ";
    cnt = check(deep_copy_stones, k); // parametric search
    // cout << "\n" << "\n";
    
    if(cnt==0){
      start = mid + 1;
    }else if(cnt==1){
      ans = mid;
      break;
    }else{
      end = mid - 1;
    }

  }
  return ans;
};

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  vector<int> stones = {2, 4, 5, 3, 2, 1, 4, 2, 5, 1};
  auto max_stone = max_element(stones.begin(), stones.end());
  int k = 3;
  cout << search(stones, *max_stone, k);
  return 0;
};