//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int answer = 50;
bool visited[50];

bool checkWord(string a, string b) {
    int cnt = 0;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i])
            cnt++;
    }
    return (cnt == 1);
}

void dfs(string begin, string target, vector<string> words, int step) {
    if (answer <= step)
        return;
    if (begin == target) {
        answer = min(answer, step);
        return;
    }
    for (int i = 0; i < words.size(); i++) {
        if (checkWord(begin, words[i]) && !visited[i]) {
            visited[i] = true;
            dfs(words[i], target, words, step + 1);
            visited[i] = false;
        }
    }
    return;
}

int solution(string begin, string target, vector<string> words) {
    dfs(begin, target, words, 0);
    if (answer == 50) answer = 0;
    return answer;
}

int main(void) {
    vector <string> words;
    words.push_back("hot");
    words.push_back("dot");
    words.push_back("dog");
    words.push_back("lot");
    words.push_back("log");
    words.push_back("cog");
    std::cout << solution("hit", "cog", words);
    return 0;
}