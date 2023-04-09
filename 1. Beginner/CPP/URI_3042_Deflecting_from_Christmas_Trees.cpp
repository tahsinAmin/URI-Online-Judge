#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
 int test, freeLane, cnt, carPos;
 int track[3];

 while (cin >> test && test != 0)
 {
		cnt = 0;
		carPos = 1;
		for (int i = 0; i < test; i++)
		{
			cin >> track[0] >> track[1] >> track[2];
			if (track[0] == 0 && track[1] == 0 && track[2] == 0)
			{
			}
			else
			{
				auto itr = find(track, track + 3, 0);
				if (itr != end(track))
				{
					freeLane = distance(track, itr);
				}
				cnt += abs(freeLane - carPos);
				carPos = freeLane;
			}
		}
		cout
						<< cnt << "\n";
 }
 return 0;
}