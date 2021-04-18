#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
  int n, max;
  string line, word;

  cin >> n;
  while(n>0){
    max = 0;
    string a[n];
    cin.get();
    
    for (int i = 0; i < n; i++) {
      a[i] = "";
      getline(cin,line);
      stringstream words(line);
      while (words >> word)      {
        a[i] = (a[i] == "") ? word : a[i] + " " + word;
      }      
      max = (a[i].length() > max) ? a[i].length() : max;
    }

    for (int i = 0; i < n; i++) {
      while(a[i].length() != max) {
        a[i] = " " + a[i];
      }
      cout << a[i] << "\n";
    }
    cin >> n;
    if(n >0)  cout << "\n";
  }
  
  return 0;
}