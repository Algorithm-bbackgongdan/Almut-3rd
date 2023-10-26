#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool check(vector<int> stones, int mid, int k){
  int sum = 0; 
  int block = 0;
  
  // (mid-1) people cross bridge
  vector<int> deep_copy_stones = stones;
  for(int i=0;i<deep_copy_stones.size();i++){
    deep_copy_stones[i] = deep_copy_stones[i] - (mid-1)<0 ? 0 : deep_copy_stones[i] - (mid-1);
  };

  // for(int i=0;i<deep_copy_stones.size();i++) cout  << deep_copy_stones[i] << " ";
  
  // check if mid people can cross bridge
  for(int i=0;i<k;i++) sum+=deep_copy_stones[i];
  if(sum==0) block+=1;
  for(int i=k;i<deep_copy_stones.size();i++){
    sum += deep_copy_stones[i] - deep_copy_stones[i-k];
    if(sum==0) block+=1;
  };
  if (block>=1)  return false; // cannot pass
  else return true; // can pass
};


int search(vector<int> stones, int high, int k){
  int start = 0;
  int end = high;
  int ans = -1;
  bool can_pass;
  while(start<=end){
    int mid = (start+end)/2;
    
    
    // cout << "start:" << start<<" ";
    // cout << "end:" << end<<" ";
    // cout << "mid:" << mid <<" "<< "\n";

    can_pass = check(stones,mid, k); // parametric search
    // cout << "\n" << "\n";
    
    if(can_pass){
      ans = max(ans, mid);
      start = mid + 1;
    }else{
      end = mid - 1;
    }
  };  
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