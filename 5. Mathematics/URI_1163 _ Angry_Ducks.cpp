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


int main(){
    int p1, p2, n;
    double h0,h, angle, v, vx,vy, a, b, c, t1, t2, s;
    string result;

    while(cin >> h0){
        h = 0.0;
        sc2(p1, p2);
        scan(n);

        while(n--){
            scan(angle);
            scan(v);

            vx = v*cos(angle*pi/180.0);
            vy = v*sin(angle*pi/180.0);
           // println(vx);
           // println(vy);

            c = h + h0;
            b = vy;
            a = 0.5 * g;

            //println(a);
            //println(b);
            //println(c);

            t1 = (-b + sqrt(pow(b,2) - 4*a*c))/ (2*a);
            t2 = (-b - sqrt(pow(b,2) - 4*a*c))/ (2*a);
            //println("");
            //println(t1);
            //println(t2);

            s=vx;
            s *= (t1 > 0.0) ? t1:t2;
            result = (s >=p1 && s<=p2) ? " -> DUCK" : " -> NUCK";
            cout << fixed <<  setprecision(5) << s << result <<"\n";
        }
    }
    return 0;
}
