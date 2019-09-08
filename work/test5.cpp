#include <iostream>

using namespace std;

int main(){
    int i;
    char ch;
    FILE *fp1;;
    fp1 = fopen("zrf.dat", "w");
    cin >> ch;
    while(ch!='*'){
        fputc(ch,fp1);
        cin >> ch;
    }
    fclose(fp1);
    if((fp1 = fopen("zrf.dat", "r")) == NULL){
        cout << "\nbuneng" << endl;
        exit(1);
    }
    while ((ch=fgetc(fp1))!=EOF)
    cout << ch;
    fclose(fp1);
    return 0;
}