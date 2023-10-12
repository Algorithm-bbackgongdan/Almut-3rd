// C++ 풀이
#include <string>
#include <iostream>
#include <vector>
#define MAX 1000000000

using namespace std;

int answer = MAX;

int different_alphabets_num(string a, string b) {
    int cnt = 0;
    for(int i = 0 ; i < a.length() ; i++) {
        if (a[i] != b[i]) cnt++;
    }
    return cnt;
}

void dfs(int cnt, string begin, string target, vector<string> words, vector<bool> visited) {
    if (begin.compare(target) == 0) {
        answer = min(answer, cnt);
        return;
    }
    for(int i = 0 ; i < visited.size() ; i++) {
        if (visited[i]) continue;
        if (different_alphabets_num(words[i], begin) == 1) {
            visited[i] = true;
            dfs(cnt + 1, words[i], target, words, visited);
            visited[i] = false;
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    vector<bool> visited(words.size(), false);
    dfs(0, begin, target, words, visited);
    if (answer == MAX) answer = 0;
    return answer;
}