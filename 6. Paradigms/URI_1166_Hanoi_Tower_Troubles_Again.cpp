#include <stdio.h>
#include <bits/stdc++.h>
#include <iostream>
#include <math.h>

using namespace std;

#define scan(x) cin>>x
#define println(x) cout<<x<<"\n";

int t, pegs, ball, magic, n;
const int limit = 51;
int store[limit];

int main(){

    for(int pegs =1; pegs< limit; pegs++){
        ball = 1;
        int arr[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        for(int j =1; j<= pegs;){
            if(arr[j] == 0){
                arr[j] = ball;
                j=1;
                ball++;
            }else{
                magic = (int)(sqrt(ball+arr[j]));
                if(((magic*magic) == (ball+arr[j])) == 1){
                    arr[j] = ball;
                    ball++;
                    j=1;
                }else{
                    j++;
                }
            }
        }
        store[pegs] = ball-1;
    }

    scan(t);
    while(t--){
        scan(n);
        println(store[n]);
    }
    return 0;
}
