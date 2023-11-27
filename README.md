# 알고리즘 멋쟁이 3기

# 목표

- 기업 코딩테스트에 자주 출제되는 문제 유형을 빠르게 익히고 합격할 역량 기르기

# 진행 기간 및 내용

스터디의 텐션과 시험 기간을 고려하여 8주 분량의 시즌제를 생각했습니다.

그리디, 구현, DFS/BFS, 정렬, 이진탐색, DP, 최단경로, 그래프 등 유형 연습 문제(백준)와 유형을 모르는 실전 문제(프로그래머스)를 풉니다.

- 참고 교재
  1기, 2기 스터디 때 **_이것이 취업을 위한 코딩 테스트다_** 교재를 활용했습니다. 위에 언급한 유형들은 교재의 목차에 해당합니다.
  [이것이 취업을 위한 코딩 테스트다 with 파이썬 - YES24](http://www.yes24.com/Product/Goods/91433923)

| 주차 | 기간          | 내용                                                    | 총 문제 수 |
| ---- | ------------- | ------------------------------------------------------- | ---------- |
| 1    | 10/2 - 10/8   | 그리디, 구현 백준 각 1문제                              | 2          |
| 2    | 10/9 - 10/15  | DFS/BFS, 정렬 백준 각 1문제 + 프로그래머스 1문제        | 3          |
| 3    | 10/30 - 11/5  | 이진탐색, DP 백준 각 1문제 + 프로그래머스 1문제         | 3          |
| 4    | 11/6 - 11/12  | 최단경로, 그래프이론 백준 각 1문제 + 프로그래머스 1문제 | 3          |
| 5    | 11/13 - 11/19 | 랜덤 유형 백준 or 프로그래머스 3문제                    | 3          |
| 6    | 11/20 - 11/26 | 랜덤 유형 백준 or 프로그래머스 3문제                    | 3          |
| 7    | 11/27 - 12/3  | 랜덤 유형 백준 or 프로그래머스 3문제                    | 3          |
| 8    | 12/4 - 12/10  | 랜덤 유형 백준 or 프로그래머스 3문제                    | 3          |

# 진행 방식

- 해당 주차 총무가 백준 + 프로그래머스 문제 출제
  - 총무는 매주 돌아가면서 바꿈
- 마감일까지 출제된 3문제 풀기 + README.md 작성 후 깃헙에 PR
  - README.md는 공부한 내용, 문제 풀이, 접근 방법 등 자유롭게 작성하시면 됩니다.
  - 문제를 못 풀었을 경우 접근 방법에 대해 회고하여 적어주세요.
- 코드 리뷰 후 merge
- 총무가 벌금 계산 후 -> 다음 주차 총무가 README.md 업데이트 (문제 출제)

# 보증금

- 어느 정도의 강제성을 부여하기 위해 `(인원 수) * (주차 수) * 300` 원을 1 인당 보증금으로 생각하고 있습니다
  스터디 완주 시 보증금은 반환됩니다
  단, 해당 주차에 **“미션”** 실패 시, 보증금에서 `(인원 수) * 300` 원이 차감됩니다.
  ex) 스터디 인원 7명, 총 8주차 스터디인 경우
  1인당 보증금 : `7 * 8 * 300 = 16,800` 원
  미션 실패한 주 당 `7 * 300 = 2,100` 원 차감
- 스터디 종료 후, 차감으로 인해 남은 보증금 잔액은 `(보증금 잔액) / (인원 수)` 만큼 배분합니다.

# 기타

- 문제풀이를 위한 언어 선택은 자유입니다.
- 코드리뷰의 편의를 위해 Readme에 풀이를 잘 작성해주세요!
- 문제를 못 풀었다면 어디까지 생각하고 접근했는지 Readme에 기록해주세요!
- 커리큘럼과 진행방식은 협의 가능합니다.
  - +) 개인적으로 알고리즘 유형을 알 수 없는 실전 문제만 풀며 감각을 끌어올리는 훈련을 하고 싶어요.
  - +) 보증금을 조금 낮추고/올리고 싶어요
- 출제 **난이도 기준**은 대략 아래와 같습니다.
  - 백준 : Silver 1,2 ~ gold 3,4 (평균 gold 5)
  - 프로그래머스 : Lv 2 ~ 4 (평균 Lv.3) (출처: 카카오 블라인드, 테크 인턴십 등)

# 진행 방식 상세

## 매 주 일정

### 0. 시작

- git clone 후 각자 github 아이디명으로 branch 파기

### 1. 월 ~ 토요일 자정

- 알고리즘 공부
- 출제된 문제 풀기
- README.md 작성
- 내 브랜치에 push
- 내 브랜치 → main으로 pull request

### 2. 일요일

- 사이클에 맞춰 해당 사람 코드 PR 리뷰
- 주차별 해당 사람 = (자신의 번호 + 해당 주차) % 인원수
- 예) 1주차-seungwookim99 : (seungwookim99(1) + 1) % n == 2 => 2번 사람 코드 PR

### 3. 월요일

- 총무가 벌금 계산
- 문제 출제 + README.md 커리큘럼에 업데이트

## 멤버 및 번호

_문제 출제자 및 총무를 위한 멤버 번호 입니다._

김승우(1) → 강진실(2) → 윤성호(3) → 조종현(4) → 김현재(5) → 최현수(6) → 전시원(7)

## 코드 리뷰 예시

1. 코드의 시간 복잡도
2. 코드의 개선 방안
3. 추천해줄 새로운 함수나 라이브러리
4. 그 외의 코멘트

## 폴더 구조

```
README.md
code
   ㄴ seungwookim99 // 자신의 github 닉네임
     ㄴ week1
       ㄴ boj_1541.py
       ㄴ boj_1461.py
       ㄴ boj_2138.py   // 백준 문제
			 ㄴ prog_12345.py // 프로그래머스 문제
       ㄴ README.md     // 1주차 README
```

# 멤버 별 제출 현황

- 총무가 PR 기준으로 월요일마다 업데이트 해주세요!
- ✅ : 미션 성공
- 😥 : 미션 실패 (지각, 미제출, 미흡)

| 멤버                                              | 1주차 | 2주차 | 3주차 | 4주차 | 5주차 | 6주차 | 7주차 | 8주차 |
| ------------------------------------------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| [seungwookim99](https://github.com/seungwooKim99) | ✅    | ✅    | ✅    | ✅    | ✅    | 😥    |       |       |
| [kauthenticity](https://github.com/kauthenticity) | ✅    | ✅    | ✅    | ✅    | 😥    | 😥    |       |       |
| [SungHo-Ck](https://github.com/SungHo-Ck)         | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    |       |       |
| [jonghyeonjo99](https://github.com/jonghyeonjo99) | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    |       |       |
| [itsnowkim](https://github.com/itsnowkim)         | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    |       |       |
| [itsme-shawn](https://github.com/itsme-shawn)     | 😥    | ✅    | ✅    | 😥    | ✅    | 😥    |       |       |
| [siwonblue](https://github.com/siwonblue)         | ✅    | ✅    | ✅    | ✅    | ✅    | 😥    |       |       |

# 커리큘럼

- 총무가 월요일마다 업데이트 해주세요!

## Week 1

- 총무 : [seungwookim99](https://github.com/seungwooKim99)

### 1. 그리디

- 문제정보 : 꿀 따기 (21758)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/21758

### 2. 구현

- 문제정보 : 로봇 시뮬레이션 (2174)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2174

## Week 2

- 총무 : [kauthenticity](https://github.com/kauthenticity)

### 1. BFS/DFS

- 문제정보 : 빙산 (2573)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2573

### 2. 정렬

- 문제정보 : 두 용액 (2470)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2470

### 3. 프로그래머스

- 문제정보 : 단어 변환 (43163)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43163

## Week 3

- 총무 : [SungHo-CK](https://github.com/SungHo-Ck)

### 1. 이진탐색

- 문제정보 : 드래곤 앤 던전 (16434)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/16434

### 2. DP

- 문제정보 : RGB거리 (1149)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1149

### 3. 프로그래머스

- 문제정보 : 징검다리 건너기 (64062)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/64062

## Week 4

- 총무 : [jonghyeonjo99](https://github.com/jonghyeonjo99)

### 1. 최단경로

- 문제정보 : 서강그라운드 (14938)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/14938

### 2. 그래프이론

- 문제정보 : 특정한 최단 경로 (1504)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1504

### 3. 프로그래머스

- 문제정보 : 파괴되지 않은 건물 (92344)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92344

## Week 5

- 총무 : [itsnowkim](https://github.com/itsnowkim)

### 1. 랜덤 유형 백준

- 문제정보 : 내 집 마련하기 (30619)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/30619

### 2. 랜덤 유형 백준

- 문제정보 : donstructive (30618)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/30618

### 3. 랜덤 유형 백준

- 문제정보 : 보물섬 (2589)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2589

## Week 6

- 총무 : [itsme-shawn](https://github.com/itsme-shawn)

### 1. 랜덤 유형

- 문제정보 : 성격 유형 검사하기 (118666)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118666

### 2. 랜덤 유형

- 문제정보 : 코딩 테스트 공부 (118668)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118668

### 3. 랜덤 유형

- 문제정보 : 등산코스 정하기 (118669)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118669

## Week 7

- 총무 : [siwonblue](https://github.com/siwonblue)

### 1. 랜덤 유형

- 문제정보 : 양팔저울(2629)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2629

### 2. 랜덤 유형

- 문제정보 : 외계인의 기타 연주(2841)
- 출처 : 백준
- 링크 :https://www.acmicpc.net/problem/2841

### 3. 랜덤 유형

- 문제정보 : 퍼즐 조각 채우기
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/84021
