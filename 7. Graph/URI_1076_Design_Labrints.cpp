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
#include <map>

/**If you want the graph to be a generic type, That means we'll define a tempate
class so that we can work with a  graph of integers, we can work with a graph of strings.*/
int cnt;
template <typename T>


class Graph{
    map<T, list<T>> l; /** This means that if we define T as int then his line will be map<int, List<int>> l;*/

public:
    void addEdge(int x, int y){
        l[x].push_back(y);
        l[y].push_back(x);
    }

    void dfs_helper(T src, map<T, bool> &visited){
        cnt++;
        visited[src] = true;
        for(T nbr : l[src]){
            if(!visited[nbr]){
                dfs_helper(nbr, visited);
                cnt++;
            }
        }
    }

    void dfs(T src){
        cnt=0;
        map<T, bool> visited;
        // Mark all the nodes as not visited in the beginning.
        for(auto p : l){
            T node = p.first;
            visited[node] = false;
        }
        dfs_helper(src, visited);
    }
};

int main(){
    int t;
    scan(t);
    while(t--){
        int start, v,e,v1,v2;
        Graph<int> g;
        scan(start);
        sc2(v,e);

        while(e--){
            sc2(v1,v2);
            g.addEdge(v1,v2);
        }

        g.dfs(start);
        printf("%i\n", cnt-1);
    }
    return 0;
}
