#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> A(10);
    int count = 0, n, i;
    cin >> n;
    A.reserve(n);
    for(i = 2; i <= n; i++)
        if(i%3 == 0 && i % 5 == 0) A[count++]= i;
        for(i = 0; i< count; i++)
        cout << A[i] << " ";
    return 0;
}
