#include<iostream>
#include<cstring>
using namespace std;

class A
{
public:
	virtual void fun() {
		cout << "A::fun()" << endl;
	}
	virtual ~A() {
		cout << "~A" << endl;
	}
};

class B :public A {
public:
	void fun() {
		cout << "B::fun()" << endl;
	}
	~B() {
		cout << "~B" << endl;
	}
};

int main() {
	A *a = new B;
	a->fun();
	delete a;
	while (1);
	return 0;
}
