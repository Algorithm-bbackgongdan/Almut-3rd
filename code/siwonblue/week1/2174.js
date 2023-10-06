const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let line = fs.readFileSync(filePath, "utf8");
let input = line.trim().split("\n");

const [A, B] = input.shift().split(" ").map(Number);
const [N, M] = input.shift().split(" ").map(Number);
const robots = Array.from({ length: N + 1 });

// get position of robots
for (let i = 0; i < N; i++) {
  const position = input[i].split(" ");
  const x = +position[0];
  const y = +position[1];
  const init = position[2];
  robots[i + 1] = [x, y, init];
}
const orders = input.slice(N);

const switchToLeft = (to) => {
  switch (to) {
    case "N":
      return "W";
    case "E":
      return "N";
    case "S":
      return "E";
    case "W":
      return "S";
  }
};
const switchToRight = (to) => {
  switch (to) {
    case "N":
      return "E";
    case "E":
      return "S";
    case "S":
      return "W";
    case "W":
      return "N";
  }
};
const forwardTo = (x, y, to) => {
  switch (to) {
    case "N":
      return [x, y + 1, to];
    case "E":
      return [x + 1, y, to];
    case "S":
      return [x, y - 1, to];
    case "W":
      return [x - 1, y, to];
  }
};

const operations = {
  L: (x, y, to) => [x, y, switchToLeft(to)],
  R: (x, y, to) => [x, y, switchToRight(to)],
  F: (x, y, to) => forwardTo(x, y, to),
};

function solution() {
  for (let i = 0; i < orders.length; i++) {
    const order = orders[i].split(" ");
    const xIndex = +order[0];
    const operation = order[1];
    const repeat = +order[2];

    let [x, y, to] = robots[xIndex];

    for (let j = 0; j < repeat; j++) {
      const [x_, y_, to_] = operations[operation](x, y, to);

      // check out of range
      if (x_ > A || y_ > B || x_ < 1 || y_ < 1)
        return `Robot ${xIndex} crashes into the wall`;

      // check other robots
      let msg = "";
      robots.map((robot, yIndex) => {
        if (yIndex !== xIndex && yIndex !== 0) {
          const [other_x, other_y] = robot;
          if (other_x === x_ && other_y === y_) {
            msg = `Robot ${xIndex} crashes into robot ${yIndex}`;
            return;
          }
        }
      });

      if (msg) return msg;

      // pass
      x = x_;
      y = y_;
      to = to_;
      robots[xIndex] = [x, y, to];
      // console.log("updated operation, x,y,to", x, y, to);
    }
  }
  return "OK";
}

console.log(solution());
