
#include <iostream>
using namespace std;

int n;
int a[51];

int solve(){
	int profit,  maxProfit;
	profit = maxProfit = 0;
	for (int i = 0 ; i < n ; i++)	{
		profit = max(0, profit + a[i]);
		maxProfit = max(maxProfit, profit);
	}
	return maxProfit;
}

int main(){
	int cost;
	while(cin >> n)	{
		cin >> cost;
		for (int i = 0 ; i < n ; i++)		{
			cin >> a[i];
			a[i]-= cost;
		}
		cout << solve() << '\n';
	}
}

//  https://en.wikipedia.org/wiki/Maximum_subarray_problem
//  https://www.youtube.com/watch?v=tinz1fiYv0c