#define println(x) cout<<x<<"\n";
#define scan(x) cin >> x;
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int GCD(int a, int b){
	if(b == 0) return a;
	else GCD(b,a%b);
}

int main(){
    int den, num;
    int n, n1, d1, n2, d2;
    char c1, c2, c3;

    den=0;
    num=0;

    scan(n);
    for(int i = 0; i < n;i++){
        scanf("%i %c %i %c %i %c %i", &n1, &c1, &d1, &c2, &n2, &c3, &d2);

        if(c2 == '+'){
            den = d1 * d2;
            num = (n1 * d2) + (n2 * d1);
        }else if(c2 == '-'){
            den = d1 * d2;
            num = (n1 * d2) - (n2 * d1);
        }else if(c2 == '*'){
            den = d1 * d2;
            num = n1 * n2;
        }else if(c2 == '/'){
            den = d1 * n2;
            num = n1 * d2;
        }

        int gC = GCD(num, den);
        gC *= (gC<0) ? -1 : 1;
        if(gC == 0){
            printf("%i/%i = %i/%i\n", num,den,num,den);
        }else{
            printf("%i/%i = %i/%i\n", num,den, num/gC,den/gC);
        }

    }
    return 0;
}
