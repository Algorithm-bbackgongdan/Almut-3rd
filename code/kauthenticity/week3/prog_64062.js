function solution(stones, k) {
  var answer = 0;
  let left = stones.reduce(
    (minVal, cur) => (minVal < cur ? minVal : cur),
    stones[0]
  );
  let right = stones.reduce(
    (maxVal, cur) => (maxVal > cur ? maxVal : cur),
    stones[0]
  );

  while (left <= right) {
    const mid = Math.floor((left + right) / 2); // 건널 수 있는 사람 수

    let zeroDist = 0;
    for (let i = 0; i < stones.length; i++) {
      if (stones[i] - mid <= 0) {
        zeroDist++;
      } else {
        zeroDist = 0;
      }

      if (zeroDist === k) {
        break;
      }
    }

    if (zeroDist === k) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  answer = left;

  return answer;
}
