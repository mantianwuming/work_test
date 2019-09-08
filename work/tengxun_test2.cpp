#include <bits/stdc++.h>
using namespace std;
const int maxn=1e5+10;
const int mod=1e9+7;
int dp[maxn];
int sum[maxn];
int main()
{
    int n,k;
    cin>>n>>k;
    for(int i=0;i<=maxn;i++)
    {
        dp[i]=1;
    }
    for(int i=k;i<maxn;i++)
    {
        dp[i]=dp[i-1]+dp[i-k];
        dp[i]%=mod;
    }
    sum[0]=0;
    for(int i=1;i<maxn;i++)
    {
        sum[i]=sum[i-1]+dp[i];
        sum[i]%=mod;
    }
    for(int i=0;i<n;i++)
    {
        int l,r;
        scanf("%d%d",&l,&r);
        printf("%d\n",(sum[r]-sum[l-1]+mod)%mod );
    }
}
