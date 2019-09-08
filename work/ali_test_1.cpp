#include<iostream>
using namespace std;

int nums[101];
int n;	//数组元素个数
int m;	//数组中存在n个元素和为m
bool flag;

void sum(int n,int m)   //求数组中是否存在一些元素和等于m
{
	if(nums[n] == m) flag = true;  //假设数组的最后一个元素等于和m，将flag变量置为true
	else if(n == 1) return;    //搜索完了整个数组返回
	else
	{
		sum(n-1,m-nums[n]);   //说明取了nums[n]元素
		sum(n-1,m);	//说明没有取nums[n]
	}
}

int main()
{
	cin>>n;
	for(int i =1;i<=n;i++)
	{
		cin>>nums[i];
	}
	cin>>m;
	flag = false; //初始时，将flag置为false，当找到某些元素和为m的时候在sum函数中flag的值将改变
	sum(n,m);
	if(flag)
	cout<<"Yes"<<endl;
	else
	cout<<"No"<<endl;
	return 0;
}
