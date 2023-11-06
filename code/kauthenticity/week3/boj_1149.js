const readline = require("readline");
const lines = [];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const [R, G, B] = [0, 1, 2];

function solution(n, costs) {
  let answer = Number.MAX_SAFE_INTEGER;
  const dp = Array(n)
    .fill()
    .map(() =>
      Array(3)
        .fill()
        .map(() => Array(3).fill(Number.MAX_SAFE_INTEGER))
    ); // dp[i][c1][c2]: i번 집이 c1, i-1번집이 c2색일때 최소 비용

  dp[0][R][G] = costs[0][R];
  dp[0][R][B] = costs[0][R];

  dp[0][G][R] = costs[0][G];
  dp[0][G][B] = costs[0][G];

  dp[0][B][G] = costs[0][B];
  dp[0][B][R] = costs[0][B];
  costs.forEach(([r, g, b], i) => {
    if (i === 0) {
      return;
    }

    dp[i][R][G] = Math.min(dp[i - 1][G][R], dp[i - 1][G][B]) + r;
    dp[i][R][B] = Math.min(dp[i - 1][B][R], dp[i - 1][B][G]) + r;

    dp[i][G][R] = Math.min(dp[i - 1][R][G], dp[i - 1][R][B]) + g;
    dp[i][G][B] = Math.min(dp[i - 1][B][R], dp[i - 1][B][G]) + g;

    dp[i][B][G] = Math.min(dp[i - 1][G][B], dp[i - 1][G][R]) + b;
    dp[i][B][R] = Math.min(dp[i - 1][R][G], dp[i - 1][R][B]) + b;
  });

  dp[n - 1].flat().forEach((cost) => {
    answer = Math.min(cost, answer);
  });

  return answer;
}

rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  // 읽은 데이터 처리
  [nInput, ...costInput] = lines;
  const n = Number(nInput);
  const costs = costInput.map((ci) => ci.split(" ").map((c) => Number(c)));

  console.log(solution(n, costs));

  process.exit();
});
