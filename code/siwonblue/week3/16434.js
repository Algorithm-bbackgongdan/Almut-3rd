const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/jeonsiwon/Desktop/Almut-3rd/code/siwonblue/week3/input.txt";
const input = require("fs")
  .readFileSync(filePath, "utf-8")
  .toString()
  .trim()
  .split("\n");
let [N, attack] = input[0].split(" ").map(Number);
const me = { max: -1, cur: -1, attack };
const maxHp = 10 ** 12 * 123456;

function getRoomInfo() {
  const rooms = [];
  for (let i = 1; i <= N; i++) {
    const [type, first, second] = [...input][i].split(" ").map(Number);
    const roomsInfo = { type };
    if (type === 1) {
      roomsInfo["attack"] = first;
      roomsInfo["stemina"] = second;
    } else {
      roomsInfo["buff"] = first;
      roomsInfo["potion"] = second;
    }
    rooms.push(roomsInfo);
  }
  return rooms;
}

function train(rooms) {
  let killDragon = true;
  for (let i = 0; i < rooms.length; i++) {
    const room = rooms[i];
    const { type } = room;
    // console.log("me", me);
    // console.log("room", room);
    if (type === 1) {
      let fightCount = 0;
      // fight simulation
      while (true) {
        fightCount += 1;
        room.stemina -= me.attack;
        if (room.stemina <= 0) break;

        me.cur -= room.attack;
        if (me.cur <= 0) {
          // console.log(`die in room ${i + 1}`);
          return { killDragon: false };
        }
      }
      // console.log(`${fightCount} fight and win`);
    } else {
      const { buff, potion } = room;
      me.attack += buff;
      me.cur += potion;
      if (me.cur >= me.max) me.cur = me.max;
    }

    // console.log(`room ${i + 1} ends and my condition is `, me);
    // console.log(`\n`);
  }
  return { killDragon };
}

function solution() {
  let start = 1;
  let end = maxHp;
  let ans = 10 ** 12;

  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    me.cur = mid;
    me.max = mid;
    me.attack = attack;
    const rooms = getRoomInfo();

    const { killDragon } = train(rooms);

    if (killDragon) {
      // console.log("mid", mid);
      // console.log("me:", me);
      ans = Math.min(ans, mid);
      end = mid - 1;
    } else start = mid + 1;
  }
  return ans;
}

console.log(solution());
