#include<iostream>
using namespace std;

int nums[101];
int n;	//����Ԫ�ظ���
int m;	//�����д���n��Ԫ�غ�Ϊm
bool flag;

void sum(int n,int m)   //���������Ƿ����һЩԪ�غ͵���m
{
	if(nums[n] == m) flag = true;  //������������һ��Ԫ�ص��ں�m����flag������Ϊtrue
	else if(n == 1) return;    //���������������鷵��
	else
	{
		sum(n-1,m-nums[n]);   //˵��ȡ��nums[n]Ԫ��
		sum(n-1,m);	//˵��û��ȡnums[n]
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
	flag = false; //��ʼʱ����flag��Ϊfalse�����ҵ�ĳЩԪ�غ�Ϊm��ʱ����sum������flag��ֵ���ı�
	sum(n,m);
	if(flag)
	cout<<"Yes"<<endl;
	else
	cout<<"No"<<endl;
	return 0;
}
