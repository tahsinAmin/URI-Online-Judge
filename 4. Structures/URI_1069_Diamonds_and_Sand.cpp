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
    int n, len, cnt, tmp;
    string s;

    scan(n);

    while(n--){
        scan(s);
        len = s.length();
        cnt=0;
        tmp=0;

        for(int j=0;j < len; j++){
            if(s[j] == '<') tmp++;
            if(s[j] == '>' && tmp > 0){
                tmp--;
                cnt++;
            }
        }
        println(cnt);
    }
    return 0;
}
