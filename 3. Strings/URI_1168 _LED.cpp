#include <cstdio>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <bits/stdc++.h>
#include <iostream>
#include <math.h>

using namespace std;

#define sc2(a, b) scanf("%d%d", &a, &b)
#define scan(x) cin>>x
#define fr(i, a, n) for(int i = (a); i < (n); i++)
#define println(x) cout<<x<<"\n";

#include <list>
#include <unordered_map>

int main(){

    int n, j;
    char s[101];
    long long leds;

    scan(n);

    while(n--){
        scanf("%s", &s);
        j=0;
        leds=0;
        while(true){
            if(s[j] == '1') leds+=2;
            else if(s[j] == '2') leds+=5;
            else if(s[j] == '3') leds+=5;
            else if(s[j] == '4') leds+=4;
            else if(s[j] == '5') leds+=5;
            else if(s[j] == '6') leds+=6;
            else if(s[j] == '7') leds+=3;
            else if(s[j] == '8') leds+=7;
            else if(s[j] == '9') leds+=6;
            else if(s[j] == '0')  leds+=6;
            else break;
            j++;
        }
        printf("%lld leds\n", leds);
    }

    return 0;
}
