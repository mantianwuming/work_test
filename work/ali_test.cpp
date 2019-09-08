#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

// 数组中任意几个元素的和是否等于m

using namespace std;

vector<int> addSum(vector<int> & v,int dest_sum)
{
	typedef int Value;
	typedef int Loc;
	sort(v.begin(), v.end());
	stack<pair<Value,Loc>> sta;
	int loc = 0;
	int init_loc = 0;
	int sum = v[loc];
	sta.push({ v[loc],loc});
	++loc;
	while (sum != dest_sum)
	{
		if (loc < v.size() && sum + v[loc] <= dest_sum)
		{
			sum += v[loc];
			sta.push({ v[loc], loc });
			++loc;
		}
		else
		{
			if (!sta.empty())
			{
				auto v = sta.top();
				sum -= v.first;
				sta.pop();
				loc = v.second + 1;
			}
			else
			{
				sum = 0;
				loc = ++init_loc;
			}
		}
	}

	vector<int> res;
	while (!sta.empty())
	{
		res.push_back(sta.top().first);
		sta.pop();
	}
	return res;
}

int main() {
    int arr[] = {1,2,3,4,5,6};
    vector<int> vec(arr, arr + sizeof(arr)/sizeof(int));
    int s = 50;
    vector<int> res = addSum(vec, s);
    for(int i = 0; i < res.size(); i++)
        cout << res[i] << " ";
    cout << endl;
    return 0;
}
