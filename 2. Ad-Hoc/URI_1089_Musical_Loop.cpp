#include <iostream>
using namespace std;

int main()
{

  int n, cnt, a, b, c;
  while (cin >> n && n != 0)
  {
    cnt = 0;
    int h[n];
    for (int i = 0; i < n; i++)
    {
      cin >> h[i];
    }
    if (n == 2 && h[0] != h[1])
    {
      cnt = 2;
    }
    else
    {
      for (int i = 0; i < n; i++)
      {
        a = i;
        b = (i + 1) % n;
        c = (i + 2) % n;
        if ((h[a] > h[b] && h[b] < h[c]) || (h[a] < h[b] && h[b] > h[c]))
        {
          cnt++;
        }
      }
    }
    cout << cnt << "\n";
  }
  return 0;
}