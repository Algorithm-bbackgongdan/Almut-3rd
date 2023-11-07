class Solution {
  private boolean isPossible(int n, int[] stones, int k) {
      int count = 0;
      for(int i = 0 ; i < stones.length ; i++) {
          if (stones[i] < n){
              if (++count == k) return false;
          }
          else count = 0;
      }
      return true;
  }
  
  public int solution(int[] stones, int k) {
      int answer = 0;
      int left = 1, right = 200000000, mid;
      while (left <= right) {
          mid = (left + right) / 2;
          if (isPossible(mid, stones, k)) {
              left = mid + 1;
              answer = mid;
          } else {
              right = mid - 1;
          }
      }
      return answer;
  }
}