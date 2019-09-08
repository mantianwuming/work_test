#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int minSwap(int num1){
    vector<int> a;
    vector<int> b;
    double num2 = 0;
    int num = num1;
    while(num1 != 0){
        b.push_back(num1%10);
        num1 /= 10;
    }

    reverse(b.begin(), b.end());

    for(int i = 0; i < b.size(); i++){
        a.push_back(b[i]);
    }

    sort(a.begin(), a.end());

    if(a == b){
        return num;
    }
    int i = 0, l = b.size();
    while(i < l){
        if(a[i] == b[i])
            i += 1;
        else
            break;
    }
    for(int j = l-1; j >= 0; j--){
        if(b[j] == a[i]){
            b[j] = b[i];
            b[i] = a[i];
            break;
        }
    }

    for(int i = 0; i < b.size(); i++){
        num2 += b[i] * pow(10, b.size() - i - 1);
    }
    return num2;
}

int main(){
    int num1, k;
    cin >> num1;
    cin >> k;
    for(int i = 0; i < k; i++){
        num1 = minSwap(num1);
    }
    cout << num1;
    return 0;
}

