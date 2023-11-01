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
