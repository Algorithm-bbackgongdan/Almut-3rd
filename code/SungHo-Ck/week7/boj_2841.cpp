#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N,P;

int main()
{
    int cnt = 0;
    cin >> N >> P;
    vector<vector<int>> stack = vector<vector<int>>(N, vector<int>(1, 0));
    
    for(int i=0;i<N;i++){
        int l, p;
        cin >> l >> p;
        while(stack[l - 1].back()>p){
            stack[l - 1].pop_back();
            cnt++;
        }
        if(stack[l - 1].back()==p){
            continue;
        }
        stack[l - 1].push_back(p);
        cnt++;
    }
    
    cout << cnt << endl;

    return 0;
}