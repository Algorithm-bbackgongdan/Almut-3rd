let targetAlp = 0;
let targetCop = 0;

function solution(alp, cop, problems) {
  for (let i = 0; i < problems.length; i++) {
    const p = problems[i];
    targetAlp = Math.max(targetAlp, p[0]);
    targetCop = Math.max(targetCop, p[1]);
  }
}
