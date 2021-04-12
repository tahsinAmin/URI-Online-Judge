#include <iostream>
using namespace std;
#include <list>

int main(){

  int test, multiple;
  char c;
  int arr[5];

  while(cin >> test && test!=0){
    while(test--){
      cin >> arr[0] >> arr[1] >> arr[2] >> arr[3] >> arr[4];
      multiple=0;
      for (int i = 0; i < 5; i++){
        if(arr[i] <=127){
          multiple++;
          if (multiple <=1){
            c = (i == 0) ? 'A' : (i == 1) ? 'B' : (i == 2) ? 'C' : (i == 3) ? 'D' : 'E';
          }else{
            break;
          }
        }
      }
      if (multiple ==1){
        cout << c << "\n";
      }else{
        cout << "*" << "\n";
      }
    }
  }
  return 0;
}