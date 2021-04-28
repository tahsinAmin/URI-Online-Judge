#include <iostream>
using namespace std;

int main(){
  int a, b, carry, extra;

  while(cin >> a >> b && (a || b)){
    carry = extra = 0;

    while(a || b){
      if (((a%10) + (b%10) + extra) > 9){
        carry ++;
        extra=1;
      } else extra = 0;
      a = a/10;
      b = b/10;
    }

    if (carry == 1) cout <<"1 carry operation."<< "\n";
    else if (carry > 1) cout << carry << " carry operations."<< "\n";
    else cout <<"No carry operation."<< "\n";
  }
  return 0;
}