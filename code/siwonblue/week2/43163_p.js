const begin = "hit";
const target = "cog";
// const words = ["hot", "dot", "dog", "lot", "log", "cog"];
const words = ["hot", "dot", "dog", "lot", "log", "cog"];

/**
 *  EXCEPT 1 : words does not have target
 *  EXCEPT 2 : cannot find answer after searching
 */

// O(N^3) : 10 * 10 * 50
function getSameWordsExceptOne(currentWord, words) {
  const sameWordsExceptOne = [];
  currentWord.split("").forEach((_, curIdx) => {
    for (let i = 0; i < words.length; i++) {
      if (currentWord === words[i]) continue;

      const word = words[i];
      let find = true;

      for (let wordIdx = 0; wordIdx < word.length; wordIdx++) {
        if (curIdx === wordIdx) continue;
        if (currentWord[wordIdx] !== word[wordIdx]) find = false;
      }
      if (find) sameWordsExceptOne.push({ word, difIdx: curIdx });
    }
  });

  return sameWordsExceptOne;
}

function solution(begin, target, words) {
  let answer = 0;
  // EXCEPT 1
  if (!words.includes(target)) return 0;

  const stack = [{ word: begin, count: 0 }];

  // BFS
  while (stack.length) {
    const { word, count } = stack.shift();
    const sameWordsExceptOne = getSameWordsExceptOne(word, words);

    for (let i = 0; i < sameWordsExceptOne.length; i++) {
      const { word, difIdx } = sameWordsExceptOne[i];
      if (word === target) {
        answer = count + 1;
        break;
      }
      stack.push({ word, count: count + 1 });
    }

    if (answer) return answer;
  }
  // EXCEPT 2
  return answer;
}
console.log(solution(begin, target, words));
