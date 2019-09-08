#include <stdio.h>
 
void combination(int* input,int inputLen,int m,int* out,int outLen,int* volume,int reactorCap,int* masses,int criticalMass,int numberOfRadLiquid,int* energies,int* energiesMax ) 
{
	//函数的含义是：获取数组input前inputLen部分的长度为m的组合数，并存储到out数组中
	//@input 输入待组合的数据，本例是{0,1,2,3,4}，数字代表数组的位置
	//@inputLen 截取input的前inputLen部分，比如inputLen=3，则截取input为{0,1,2}
	//@m 获取长度为m的组合，比如m=2,inputLen=3，则可能的情况有：{0,1}{0,2}{1,2}
	//@out 最后可能组合的结果。比如最开始输入，m=3，则out可能为{1,2,3}{1,2,4}等
	//@outLen out的长度
	//其余参数均为题目所给
	int j;
	if(m==0) // 退出递归，已取到一种情况
	{
		//判断该种情况下的能量和是否最大，同时又满足约束条件
		int volumeSum=0,massesSum=0,energiesSum=0;
		for(j=0;j<outLen;j++) 
		{
			volumeSum+=volume[out[j]];
			massesSum+=masses[out[j]];
			energiesSum+=energies[out[j]];
		}
		if(volumeSum<=reactorCap&&massesSum<=criticalMass)// 是否满足约束条件
		{
			if(energiesSum>energiesMax[0]) // 判断是否比上一个存储的值大
			{
				energiesMax[0]=energiesSum;
				for(int j=0;j<outLen;j++) //
				{
					printf("%d",out[j]);//输出能量最大时的组合
					printf(" ");
						
				}
				printf("%d",energiesMax[0]); //输出最大能量
				printf("\n");
			}
		}
			
		return;
	}
		
	for(int i=inputLen;i>=m;i--) //循环递归获取组合数
	{
		out[m-1]=input[i-1];
		combination(input, i-1, m-1, out, outLen,
				volume, reactorCap, masses, criticalMass, numberOfRadLiquid, energies,energiesMax);
	}
}
 
void getMaxEnergies(int* volume,int reactorCap,int* masses,int criticalMass,int numberOfRadLiquid,int* energies,int* energiesMax)
{
	int i;
	int input[numberOfRadLiquid]; //构造待组合的数据
	for(i=0;i<numberOfRadLiquid;i++)   //对应上面数据，input={0,1,2,3,4}
	{
		input[i]=i;
	}
		
	for(i=1;i<=numberOfRadLiquid;i++) //最大能量可能是由1、2、3、4、5个数据之和
	{
		int out[i];
		combination(input,numberOfRadLiquid,i,out,i, volume, reactorCap, masses, criticalMass, numberOfRadLiquid, energies,energiesMax);
	}
}
	
 
 
 
int main() 
{	
	int reactorCap=100; //反应堆的容量（V）
	int numberOfRadLiquid=5;  //现有小瓶数量（N）
	int criticalMass=15;  //反应堆的最大临界质量（M）
	int volume[5]= {50,40,30,20,10};//体积
	int masses[5]= {1,2,3,9,5};//质量
	int energies[5]= {300,480,270,200,180}; //能量
	int energiesMax[1]={0}; //输出最大能量
		
	getMaxEnergies(volume,reactorCap,masses,criticalMass,numberOfRadLiquid,energies,energiesMax);
	printf("最大能量为");
	printf("%d",energiesMax[0]);
}