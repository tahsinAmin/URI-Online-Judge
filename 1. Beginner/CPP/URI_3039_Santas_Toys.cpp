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

#include <list>



int main(){
    int n, cnt,temp;
    string st;
    scan(n);
    char c;
    temp = n;
    cnt=0;
    while(n--){
       //scanf("%s %c", &st, &c);
       cin >> st >> c;

       cnt += (c == 'M')? 1 : 0;
    }
    printf("%i carrinhos\n%i bonecas\n", cnt, (temp-cnt));
    return 0;
}
