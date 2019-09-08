#include <iostream>
#include <cstdio>

int main(){
    unsigned int a = 0x1234;
    a = ((a & 0x5555) << 1) | ((a & 0xaaaa) >> 1);
    printf("0x%x", a);
}