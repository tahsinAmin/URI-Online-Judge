#include <iostream>
#define println(x) cout<<x<<"\n";
#include <math.h>
using namespace std;

int main(){
    unsigned int n, m;

    while(scanf("%u %u", &n, &m) != EOF){
        printf("%u\n", n ^ m);
    }
    return 0;
}
