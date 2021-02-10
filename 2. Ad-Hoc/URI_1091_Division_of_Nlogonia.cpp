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
    int n, nx,ny,x,y;

    while(scan(n) && n){
        sc2(nx,ny);
        while(n--){
            sc2(x,y);
            if(x == nx || y == ny){
                println("divisa");
            }else if(x > nx && y > ny){
                println("NE");
            }else if(x < nx && y > ny){
                println("NO");
            }else if(x > nx && y < ny){
                println("SE");
            }else if(x < nx && y < ny){
                println("SO");
            }
        }
    }
    return 0;
}
