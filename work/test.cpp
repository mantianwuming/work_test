#include <bits/stdc++.h>
#include <iostream>
#include <queue>
using namespace std;
// int main(){
//     stack<int> s;
//     queue<int> q;
//     for(int i = 1; i<= 100; ++i){
//         s.push(i);
//         q.push(i);
//     }
//     long long ans = 0;
//     for(int i = 1; i <= 100; ++i)
//     {
//         ans += s.top() - q.front();
//         s.pop();
//         q.pop();
//     }
//     cout << ans << endl;
//     return 0;
// }

void push(deque<double> & values){
    values.push_front(1.1);
    values.push_front(2.1);
    values.push_back(3.1);
    values.push_back(4.1);
}
int main(){
    deque<double> values;
    ostream_iterator<double> output(cout, " ");
    push(values);
    values.pop_front();
    values[1] = 5.4;
    copy(values.begin(), values.end(), output);
    cout << endl;
    return 0;
}