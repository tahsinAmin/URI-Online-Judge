#include <cstdio>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <bits/stdc++.h>
#include <iostream>
#include <math.h>

using namespace std;

#define sc2(a, b) scanf("%d%d", &a, &b)
#define scan(x) cin>>x;
#define fr(i, a, n) for(int i = (a); i < (n); i++)
#define println(x) cout<<x<<"\n";
#define g -9.80665
#define pi 3.14159

int cnt;

int fib(int num){
    cnt++;
    if(num == 1) return 1;
    if(num == 0) return 0;
    return fib(num-1) + fib(num-2);
}

int main(){
    int n, x, calls;
    scan(n);

    while(n--){
        scan(x);
        cnt = 0;
        calls = fib(x);
        printf("fib(%i) = %i calls = %i\n", x, cnt-1, calls);
    }
    return 0;
}
