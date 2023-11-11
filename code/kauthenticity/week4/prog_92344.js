function solution(board, skill) {
    var answer = 0;
    const [n, m] = [board.length, board[0].length];
    const tempBoard = Array(n + 1)
        .fill()
        .map(() => Array(m + 1).fill(0));

    skill.forEach(([type, r1, c1, r2, c2, degree]) => {
        tempBoard[r1][c1] += type === 2 ? degree : -degree;
        tempBoard[r1][c2 + 1] += type === 2 ? -degree : degree;

        tempBoard[r2 + 1][c1] += type === 2 ? -degree : degree;
        tempBoard[r2 + 1][c2 + 1] += type === 2 ? degree : -degree;
    });

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m - 1; j++) {
            tempBoard[i][j + 1] += tempBoard[i][j];
        }
    }

    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n - 1; i++) {
            tempBoard[i + 1][j] += tempBoard[i][j];
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            board[i][j] += tempBoard[i][j];

            if (board[i][j] > 0) {
                answer++;
            }
        }
    }
    return answer;
}
