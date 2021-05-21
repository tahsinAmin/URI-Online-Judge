#include <iostream>
#include <string.h>
using namespace std;

int main()
{
  string s1, s2, result;
  int dif, test;
  cin >> test;
  while (test--)
  {
    result = "nao encaixa";
    cin >> s1 >> s2;
    dif = s1.length() - s2.length();
    if (dif >= 0)
    {
      result = (s1.substr(dif).compare(s2) == 0) ? "encaixa" : result;
    }
    cout << result << "\n";
  }
  return 0;
}