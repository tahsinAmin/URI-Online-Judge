#include <iostream>
#define println(x) cout<<x<<"\n";
#include <math.h>
using namespace std;

int main(){
    int N,x,d, sumJ, sumM;
    string result;
    cin >> N;
    while(N--){
        sumJ=0;
        sumM=0;
        for(int i = 0; i< 6; i++){
            cin>>x>>d;
            sumJ+= (i<3) ? (x*d) : 0;
            sumM+= (i>=3) ? (x*d) : 0;
        }
        result = (sumJ >= sumM) ? "JOAO" : "MARIA";
        println(result);
    }
    return 0;
}
