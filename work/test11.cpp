#include <iostream>

using namespace std;

int main(){
    int a = 12;
    a += a -= a*a;
    cout << a<< endl;
    return 0;
}