const stones = [0, 0, 0, 3, 2, 1, 4, 2, 5, 1];
const k = 3;

function isEnd(arr, k) {
  let stop = false;
  let check = 0;
  for (let i = 0; i < k; i++) check += arr[i];
  if (check === 0) return { stop: true };
  for (let i = k; i < arr.length; i++) {
    check += arr[i] - arr[i - k];
    if (check === 0) return { stop: true };
  }
  return stop;
}

function solution(stones, k) {
  let cnt = 0;
  if (isEnd(stones, k)) return cnt;

  while (true) {
    for (let i = 0; i < stones.length; i++) {
      const stone = stones[i];
      stones[i] = stone - 1 < 0 ? 0 : stone - 1;
    }
    cnt += 1;
    if (isEnd(stones, k)) return cnt;
  }
}
console.log(solution(stones, k));
