function solution(genres, plays) {
    var answer = [];
    const playCntPerGenre = {}; // [장르]: 플레이 횟수
    const playCntPerSong = {}; // [장르]: [횟수, 번호]
    const n = genres.length;

    genres.forEach((genre, i) => {
        if (playCntPerSong[genre]) {
            playCntPerSong[genre].push([plays[i], i]);
        } else {
            playCntPerSong[genre] = [[plays[i], i]];
        }

        if (playCntPerGenre[genre]) {
            playCntPerGenre[genre] += plays[i];
        } else {
            playCntPerGenre[genre] = plays[i];
        }
    });

    Object.keys(playCntPerSong).forEach((key) => {
        playCntPerSong[key].sort(([cnt1, idx1], [cnt2, idx2]) => {
            if (cnt1 == cnt2) {
                return idx1 - idx2;
            }
            return cnt2 - cnt1;
        });
    });

    Object.entries(playCntPerGenre)
        .sort(([_, cnt1], [__, cnt2]) => {
            return cnt2 - cnt1;
        })
        .forEach(([genre]) => {
            if (playCntPerSong[genre].length == 1) {
                answer.push(playCntPerSong[genre][0][1]);
            } else {
                answer.push(
                    playCntPerSong[genre][0][1],
                    playCntPerSong[genre][1][1]
                );
            }
        });

    return answer;
}
