# 2573

https://www.acmicpc.net/problem/2573

- 접근 방식
  1. 1년마다 빙산을 녹인다.
  2. 빙산의 개수를 센다.
  3. 개수가 2개 이상이면 경과된 시간을 반환한다.
  4. 예외처리: 모두 한번에 같이 녹은 경우 0을 반환한다.
- 빙산을 녹일 때 하나씩 세면서 바로 녹이면 병렬적으로 계산이 되지 않기 때문에 각 칸마다 녹여야할 개수를 세고 한번에 업데이트해줘야 한다.
- "빙산을 녹인다", "빙산의 개수를 센다" 가 합쳐진 문제라고 볼 수 있고 각각은 단순 구현이다. 특히 빙산의 개수를 셀 때 dfs 를 사용하면 효과적이다.
- 이중 반복문이 있어도 9\*10^4 이기 때문에 시간 복잡도는 여유있는 편이다.
- 1트에 성공했지만 시간을 꽤 많이 써서 틀린 거라 생각해야할 것 같다.

# 2470

https://www.acmicpc.net/problem/2470

- 시간 복잡도를 고려하지 않는다면 아래처럼 풀이할 수 있겠지만, 문제 조건이 N=10^5 이기때문에 이중 반복문을 사용하면 해결이 불가능하다.

  ```ts
  function solution() {
    const ans = [];
    let blending = 10 ** 9;
    for (let i = 0; i < len; i++) {
      const first = liquid[i];
      for (let j = 0; j < len; j++) {
        const second = liquid[j];
        if (blending > Math.abs(first + second)) {
          blending = Math.abs(first + second);
          if (ans.length !== 0) {
            ans.pop();
            ans.pop();
          }
          ans.push(first);
          ans.push(second);
        }
        blending = Math.min(blending, Math.abs(first + second));
      }
    }
    console.log(ans, blending);
  }
  solution();
  ```

- 두 개를 선택해서 합의 절대값이 더 작은 경우가 목표이기 때문에 프로그래밍적으로 구현하기 이전에 수학적으로 조건을 고정시킬 수 있는지 확인해본다.
- GOAL : "두 개의 수를 합쳐서 절대값이 더 작은 경우"

  - 음수와 양수값이 비슷하다면 조건을 만족한다. 이를 위해 정렬을 해야하는데 sort() 함수를 사용하면 nlogn 이라 주어진 시간 내에 정렬이 가능하다.
  - 이진 탐색
    - 하나의 값을 반복문으로 돌리고, 그 값을 제외한 값들에서 이진탐색(logn) 을 수행하면 nlogn 의 시간 복잡도로 모든 케이스를 탐색할 수 있다.
    - 라고 생각하였지만 이진탐색으로 어떻게 구현해야할지 모르겠어서 포기함.
  - 투포인터
    - two pointer 를 이용해서 O(N) 으로 탐색하는 방법을 생각함.

- 접근 방식

  - sort() 이용해서 정렬한다.
  - 음수와 양수를 나눠서 두 개의 배열로 만든다.
  - 음수는 revser() 시킨다.
  - 절대값이 더 작은 쪽의 포인터를 증가시키며 루프를 돌린다.

- 예외처리 : 양수 또는 음수만 존재할 경우

  > 1트 실패

# Problem & Solution

- 음수 양수를 더하지 않고 양수끼리 또는 음수끼리에서 답이 찾아지는 경우가 존재하기 때문에 아래 경우 추가  
  [[feat] 2470 second : fail](https://github.com/Algorithm-bbackgongdan/Almut-3rd/commit/9685c56817d2c8e1833d6d461534ef20d1e7643c)

  ```ts
  // except : if answer is in only positive case
  if (positive.length >= 2 && blending > Math.abs(positive[0] + positive[1]))
    return `${positive[0]} ${positive[1]}`;

  // except : if answer is in only negative case
  if (negative.length >= 2 && blending > Math.abs(negative[0] + negative[1]))
    return `${negative[1]} ${negative[0]}`;
  ```

  > 2트 실패

- 음수에 대해 예외처리할 때 오름차순이 아니었음.  
  [[feat] 2470 third : done](https://github.com/Algorithm-bbackgongdan/Almut-3rd/commit/cfcd7c6e1e8dac0f9b1bf125fd6fcc36775d66c5)

  ```ts
  // bad
  if (positive.length === 0) return `${negative[0]} ${negative[1]}`;
  ```

  ```ts
  // good
  if (positive.length === 0) return `${negative[1]} ${negative[0]}`;
  ```

  > 3트 성공

# 43163

https://school.programmers.co.kr/learn/courses/30/lessons/43163

- 1트 성공이지만 시간을 너무 많이 쓴 것 같아 틀렸다고 봐야 할 것 같다.
- 처음에 든 단순한 아이디어가 아닐 것이라 생각해서 계속 헤맸고, 결국 그냥 그 생각대로 구현해서 성공함. (근데 구현이 조금 까다로웠다.)
- 접근 방식
  - O(N^3) 이 나와도 10 x 10 x 50 이라 시간은 여유 있었고 그래서 약간 brute force 처럼 문제를 풀었다.
  - 현재 단어가 있다면 그 단어와 한 글자만 다른 여러 단어를 모두 파악한다.
  - 그 단어들을 스택에 넣고 BFS 돌린다.
