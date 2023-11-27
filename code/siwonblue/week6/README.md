[ 6주차 ]

1. 랜덤 유형
   문제정보 : 성격 유형 검사하기 (118666)
   출처 : 프로그래머스
   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118666

- 무난한 구현
- 접근 방식

  1. 아래처럼 미리 세팅을 해둔다.

  ```ts
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
  ```

  2. 문제 조건에 따라 구현한다.

2번이랑 3번은 몰라서 카카오 공식 해설을 봤는데 구현이 잘 안되어서 조금 더 고민해보겠습니다.

2. 랜덤 유형
   문제정보 : 코딩 테스트 공부 (118668)
   출처 : 프로그래머스
   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118668

3. 랜덤 유형
   문제정보 : 등산코스 정하기 (118669)
   출처 : 프로그래머스
   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118669

```

```
