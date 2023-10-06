# 2174

- 구현문제 : 문제 주어진 그대로 옮기면 됨.
- 런타임에러 2번 나게 만든 아래 입력 방식때문에 시간 많이 씀.

  ```ts
  // bad
  let line = fs.readFileSync(filePath).toString().split("\n");
  ```

  ```ts
  // good
  let line = fs.readFileSync(filePath, "utf8");
  let input = line.trim().split("\n");
  ```

- operation 을 반복해줄 때 아래 한 줄을 추가하지 않아서 1트 실패함.

  ```ts
  robots[xIndex] = [x, y, to];
  ```

# 21758
