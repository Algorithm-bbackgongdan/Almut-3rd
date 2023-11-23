const survey = ["AN", "CF", "MJ", "RT", "NA"];
const choices = [5, 3, 2, 7, 5];

const types = ["R", "T", "C", "F", "J", "M", "A", "N"];

const table = {};
types.map((t) => (table[t] = 0));
const operation = {
  1: (table, type) => (table[type[0]] += 3),
  2: (table, type) => (table[type[0]] += 2),
  3: (table, type) => (table[type[0]] += 1),
  5: (table, type) => (table[type[1]] += 1),
  6: (table, type) => (table[type[1]] += 2),
  7: (table, type) => (table[type[1]] += 3),
};

function solution(survey, choices) {
  let ans = "";
  // test
  for (let i = 0; i < survey.length; i++) {
    const type = survey[i].split("");
    const choice = choices[i];
    console.log(choice);
    if (choice === 4) continue;
    operation[choice](table, type);
  }

  // get ans
  const temp = Object.entries(table);
  for (let i = 0; i < temp.length; i++) {
    if (i % 2 === 0) continue;
    if (temp[i - 1][1] == temp[i][1]) {
      // 문자열이 더 빠른 걸로
      ans +=
        temp[i - 1][0].charCodeAt() > temp[i][0].charCodeAt()
          ? temp[i][0]
          : temp[i - 1][0];
      continue;
    }
    // 값이 더 큰 경우
    ans += temp[i - 1][1] > temp[i][1] ? temp[i - 1][0] : temp[i][0];
  }
  return ans;
}
solution(["TR", "RT", "TR"], [7, 1, 3]);
