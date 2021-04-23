#include <iostream>
#include <queue>
using namespace std;

int main(){
  int n;

  while(cin >> n && n != 0){
    queue<int> q;

    for (int i = 1; i <=n; i++){
      q.push(i);
    }
    if(n == 1) cout << "Discarded cards:\n";	
    else cout << "Discarded cards: ";

    while(q.size() != 1){
        if(q.size() != 2) cout << q.front() << ", ";
        else cout << q.front() << "\n";
        q.pop();
        q.push(q.front()); 
        q.pop();
    }
    cout << "Remaining card: " << q.front() << endl;
  }
  return 0;
}