#include <iostream>
using namespace std;
#include <list>

class Graph
{
  list<int> *l;
  int V;

public:
  Graph(int V)
  {
    this->V = V;
    l = new list<int>[V];
  }

  void addEdge(int x, int y, bool directed = true)
  {
    l[x].push_back(y);
    l[y].push_back(x);
  }

  void connected_helper(int node, bool *visited, int parent)
  {
    visited[node] = true;
    for (auto nbr : l[node])
    {
      if (!visited[nbr])
      {
        connected_helper(nbr, visited, node);
      }
    }
  }

  bool connected()
  {
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++)
      visited[i] = false;

    connected_helper(0, visited, -1);

    for (int i = 0; i < V; i++)
      if (visited[i] == false)
        return false;

    return true;
  }
};

int main()
{
  int n, l, x, y;
  cin >> n >> l;
  Graph g(n);

  for (int i = 0; i < l; i++)
  {
    cin >> x >> y;
    x--;
    y--;
    g.addEdge(x, y);
  }

  string s = (g.connected()) ? "COMPLETO" : "INCOMPLETO";
  cout << s << "\n";
  return 0;
}