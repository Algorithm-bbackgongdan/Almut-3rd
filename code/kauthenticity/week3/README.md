# WEEK 3

## BOJ 16434

### Code

```javascript
const readline = require("readline");
const lines = [];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let max = 0;

function solution(n, warriorAttack, rooms) {
  let left = BigInt(1);
  let right = BigInt(123456 * 100000000 * 100000000);
  let answer = Infinity;

  while (left <= right) {
    const mid = (left + right) / BigInt(2);

    let [curWarriorAttack, curWarriorHP, maxWarriorHP] = [
      warriorAttack,
      mid,
      mid,
    ];
    let isWarriorDead = false;

    for (let i = 0; i < rooms.length; i++) {
      const roomType = rooms[i][0];
      const attack = BigInt(rooms[i][1]);
      const hp = BigInt(rooms[i][2]);

      if (Number(roomType) === 1) {
        let warriorAttackCnt = hp / curWarriorAttack;
        if (warriorAttackCnt * curWarriorAttack < hp) {
          warriorAttackCnt = warriorAttackCnt + BigInt(1);
        }

        curWarriorHP -= attack * (warriorAttackCnt - BigInt(1));

        if (curWarriorHP <= BigInt(0)) {
          isWarriorDead = true;
          break;
        }
      }

      if (Number(roomType) === 2) {
        curWarriorAttack += attack;
        curWarriorHP =
          maxWarriorHP < curWarriorHP + hp ? maxWarriorHP : curWarriorHP + hp;
      }
    }

    if (isWarriorDead) {
      left = mid + BigInt(1);
    } else {
      if (answer > mid) {
        answer = mid;
      }
      right = mid - BigInt(1);
    }
  }

  return answer;
}

rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  // 읽은 데이터 처리
  const [line1, ...restLines] = lines;
  const [n, warriorAttack] = line1.split(" ").map((val) => BigInt(val));
  const rooms = restLines.map((rl) => rl.split(" ").map((val) => BigInt(val)));

  console.log(Number(solution(n, warriorAttack, rooms)));
  process.exit();
});
```

### Approach

1. 용사의 최대 체력을 mid값으로 해서 이분 탐색을 한다.
2. 용사가 죽으면 최대 체력을 키우고, 살면 최대 체력을 줄인다.

위와 같은 방법으로 접근헀는데 결국엔 풀지 못했따... ㅠㅠ

### TIL

1. Javascript에서 매우 큰 수를 다루기 위해서는 `BigInt` 생성자를 써야 한다.
2. bigint type은 Math 메서드의 인수가 되지 못한다. 즉, Math.max(), Math.min(), Math.ceil()을 사용해선 안된다.

## BOJ 1149

### Code

```javascript
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
```

### Approach

1.  `dp[i][c1][c2]`: i번 집이 c1, i-1번집이 c2색일때 최소 비용 << 이렇게 정의한다.
2.  첫번째 집부터 R, G, B 전부 칠해가면서 dp 값을 갱신해 준다.

### TIL

큰 어려움 없이 풀었다.

## Programmers 64062

### Code

```javascript
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
```

### Approach

1. 건널 수 있는 최대 사람 수를 Mid로 하여 이분탐색을 한다.
2. 각 iteration마다 최대로 연속한 0의 길이를 구하고, 이게 k를 넘으면 mid를 줄인다.
3. 반대로 k 미만이면 mid를 키운다.

### TIL

처음엔 최대로 연속한 0의 길이를 찾아서 풀었는데 시간 초과가 발생했다.
단순 구현으로 시간초과가 날 것 같을때는 이분탐색으로 풀 수 있는지를 생각해야겠다. 이 문제 역시 1~최대 사람수로 오름차순 정렬이 돼 있으므로 이분탐색이 적용 가능하다.

그리고 프로그래머스 컴파일러는 Math.min(),Math.max()의 인수 개수 제한이 그렇게 크지는 않은 것 같다.
프로그래머스에서 코테를 본다면 배열의 최소(최대) 값은 Array.prototype.reduce()로 찾아야겠다.
