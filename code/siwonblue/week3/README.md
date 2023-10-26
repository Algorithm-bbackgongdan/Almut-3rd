# 16434

https://www.acmicpc.net/problem/16434

문제 분석

- 구현 + 이진 탐색
- 구현만 생각하면 유저의 체력을 1부터 시작해서 2,3,4, ... 정답까지 시도하면 된다.
- 근데 가능한 경우의 수가 10^18 라서 시간 안에 탐색이 불가능하기 때문에 이진탐색을 사용해야 한다.
- min : 1
- max : ((몬스터의 공격력 최대값) _ (몬스터의 체력 최대값 - 1) + 1) _ 방의 개수

- 이진 탐색에는 두 가지 유형이 있다. 단순히 이진탐색을 통해서 특정 값을 찾기만 하면 끝나는 경우가 쉽게 나오는 경우고, 이 문제 같은 경우 값을 찾고 문제 조건에 맞는지 다시 한번 더 검증을 해야한다. 이런 유형이 조금 더 난이도가 있고 책에서는 파라메틱 서치라고 소개하고 있다.

1트 실패  
2트 시간초과  
...  
N트 시간초과

Problem  
시뮬레이션을 할 때 무한루프로 한대씩 쳤는데 이걸 수학적으로 바꿔서 O(N) 을 O(1) 로 바꿨다. 시간초과 원인을 찾으려고 10번 시도만에 겨우 성공함..

```c++
    // bad
    while(true){
      room[2] -= me.attack;
      if(room[2]<=0) break;

      me.cur -= room[1];
      if(me.cur<=0){
        killDragon = false;
        return killDragon;
      }
    }
```

```c++
  // good
  long long t;
    if(room[2] % me.attack == 0) t = room[2]/me.attack - 1;
    else t = room[2]/me.attack;
    me.cur -= room[1] * t;
    if(me.cur <= 0) return false;
```

- 기억할 점
  1. c++ 에서는 cin cout 을 쓰면 입출력 효율을 높이기 위해 아래 코드 추가해줘야 함.
  ```c++
    ios_base::sync_with_stdio(false);
    cin.tie(0);
  ```
  2. 커질 것 같으면 `long long` 쓰자

# 1149

https://www.acmicpc.net/problem/1149

(못풀어서 답 봄)  
fail.js (실패 코드)  
ref.js (답 코드)

- 접근방식

  1. 첫번째 집을 R,G,B 로 결정하고 그 다음 값중 가장 작은 값을 계속 더한다.
     로 했는데 마지막 테스트 케이스가 통과가 안됨..

답 찾아봄.

- Problem  
  처음 들어갈 값에 RGB 모두 시도했는데 이부분에서 문제가 생긴다.
  RGB 세 가지 경우를 모두 고려하고 그 다음 값을 선택할 때 색이 다른 값중에 작을 값을 더해서 나가는 방식으로 구했는데,
  애초에 최소값이 RGB 중 하나로 시작하지 않을 수도 있음. 예를 들어 R 로 시작하지 않는 경우에서 최소값이 나올 수 있는데
  RGB 를 모두 초기 값으로 설정하고 더한 것이 문제가 되었다.

  [71 39 44] 가 초기값이면 그 다음 값을 정할 때 [ (39 와 44) 중 작은 값, (71와 44)중에 작은 값, (71와 39)중에 작은 값 ] 을 선택하게 되면
  71(R)로 시작하는 경우는 존재하지 않는다. 이 부분이 반례라서 나의 풀이가 틀렸다.

![image](https://github.com/Algorithm-bbackgongdan/Almut-3rd/assets/87080940/54150e2d-c86c-4f69-a118-e9f2c63453f9)

# 64062

https://school.programmers.co.kr/learn/courses/30/lessons/64062

1. -1씩 해주고
2. K개의 연속된 0 이 있는지 탐색한다.

- 2\* 10 \*\* 5 이기때문에 배열을 두번돌리면 시간 초과가 남.
- 슬라이딩 윈도우로 배열 탐색하면 되겠다.
- 로 이해하고 풀었는데 당연히 그럴리가 없었다.
- 정확도는 다 통과했지만 효율성을 하나도 통과못함.

Problem

- 배열의 길이가 20만이라 슬라이딩 윈도우로 한번 돌리면 탐색은 쉽다.
- 하지만 배열 원소의 범위가 2억까지 가기때문에 -1씩 해주는 부분에서 효율성이 떨어지는 것 같다. (16434 던전 문제에서 train 시뮬레이션과 유사)
- 반례 : 배열의 길이가 20만이라 상관없나 싶지만 stones = [2억, 0, 1.9억, 2억]이고 K가 2라면 아래 코드가 답을 찾기위해 1.9억번 돌아야한다.

```ts
// bad
for (let i = 0; i < stones.length; i++) {
  const stone = stones[i];
  stones[i] = stone - 1 < 0 ? 0 : stone - 1;
}
cnt += 1;
if (isEnd(stones, k)) return cnt;
```

Solution (다섯번만에 찾은)

0. 시간복잡도 : O(NlogN)
1. 이분 탐색의 파라미터는 건넌 사람수
2. n 명이 건널 수 있는지 확인한다.

- 건널 수 있다면 start 값을 올린다.
- 못건넌다면 end 값을 줄인다.

3. 건널 수 있는지 확인하는 방법 (parametric search)

- mid 값이 정해지면 (mid-1) 만큼 원소를 모두 뺀다. (mid-1 명이 건넜다고 가정하는 것)
- mid 가 건널 수 있는지 슬라이딩 윈도우를 통해 확인한다.

- c++ 잔기술

  1. vector 는 항상 deep copy 하니까 그냥 복사하면 된다. 매우편함.

  ```c++
    #include <vector>
    vector<vector<int>> test = {{1,2},{3,4}}; // original
    vector<vector<int>> deep_test = test; // deep copy
  ```
