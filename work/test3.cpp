#include <iostream>
using namespace std;
int main(){
    char c, d;
    cin >> c >> d;
    switch( c -'0'){
        case 1: switch(d % '0'){
            case 1: cout << "=";
            case 2: cout << "~";
        }
        case 2: switch(d % '0'){
            case 1: cout << "_";
            case 2: cout << "^";
        }
    }
    return 0;
}
