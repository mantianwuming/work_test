#include <bits/stdc++.h>
using namespace std;
int g[10][10], vis[10][10];
string s[5];
int n = 5;
void dfs(int i, int j){
    vis[i][j] = 1;
    if(i-1 > 0){
        if(vis[i-1][j] == 0 && s[i-1][j] == '*'){
            dfs(i-1, j);
        }
    }

    if(i +1 < n){
        if(vis[i+1][j] == 0 && s[i+1][j] == '*'){
            dfs(i+1, j);
        }
    }

    if(j-1 > 0){
        if(vis[i][j-1] == 0 && s[i][j-1] == '*'){
            dfs(i, j-1);
        }
    }

    if(j+1 < n){
        if(vis[i][j+1] == 0 && s[i][j+1] == '*'){
            dfs(i, j+1);
        }
    }
}

int main(){
    for (int i = 0; i < n; ++i){
        cin >> s[i];
    }
    int ans = 0;
    memset(vis, 0, sizeof(vis));
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            if(s[i][j] == '*' && vis[i][j] != 1){
                ans++;
                dfs(i, j);
            }
        }
    }
    cout << ans << endl;
    return 0;
}