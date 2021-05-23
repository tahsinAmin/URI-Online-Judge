#include <iostream>
#include <string.h>
using namespace std;

int main()
{
  int test, n, baseAddress, noOfKeys, val, pos;
  cin >> test;
  n = test;
  while (test--)
  {

    cin >> baseAddress >> noOfKeys;
    string storage[baseAddress];
    for (int i = 0; i < baseAddress; i++)
    {
      storage[i] = to_string(i) + " -> ";
    }

    while (noOfKeys--)
    {
      cin >> val;
      pos = val % baseAddress;
      storage[pos] += to_string(val) + " -> ";
    }
    for (int i = 0; i < baseAddress; i++)
    {
      cout << storage[i] << "\\\n";
    }
    if (test != 0)
      cout << "\n";
  }
  return 0;
}