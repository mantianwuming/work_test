#include <iostream>
#include <vector>
#include <queue>
using namespace std;


string isLegal(vector<vector<char>>& matrix, int a, int b) {
    vector<vector<int>> dirs = {{0, 1},{0, -1}, {1, 0}, {-1, 0}};
    vector<vector<bool>> visited(matrix.size(), vector<bool>(matrix[0].size(), false));
    queue<pair<int, int>> q;
    q.push(make_pair(a, b));
    visited[a][b]=true;
    while (!q.empty()) {
        auto p=q.front();
        q.pop();
        int x=p.first, y=p.second;
        for (auto& dir : dirs) {
            int nextX=x+dir[0], nextY=y+dir[1];
            if (matrix[nextX][nextY]=='.'&&!visited[nextX][nextY]) {
                if (nextX==0 or nextX==matrix.size()-1 or nextY==0 or nextY==matrix[0].size()-1) {
                    return "Yes";
                } else  {
                    q.push(make_pair(nextX, nextY));
                    visited[nextX][nextY]=true;
                }
            }
        }
    }
    return "No";
}

int main(int argc, const char * argv[]) {
    int T, n, m, a, b;
    string s;
    cin>>T;
    while (T--) {
        cin>>n>>m;
        vector<vector<char>> matrix(n*3, vector<char>(m*3));
        for (int i=0; i<n; ++i) {
            cin>>s;
            for (int j=0; j<m; ++j) {
                char c=s[j];
                for (int x=0; x<3; ++x) {
                    for (int y=0; y<3; ++y) {
                        if (c=='S') {
                            if (x==1&&y==1) {
                                matrix[n*x+i][m*y+j]=c;
                                a=n*x+i;
                                b=m*y+j;
                            } else {
                                matrix[n*x+i][m*y+j]='.';
                            }
                        }else {
                            matrix[n*x+i][m*y+j]=c;
                        }
                    }
                }
            }
        }
        cout<<isLegal(matrix, a, b)<<endl;
    }
}