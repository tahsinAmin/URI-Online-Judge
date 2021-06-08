// Presentation error

#include <iostream>
#include <string.h>
#include <queue>
using namespace std;

typedef struct node
{
  int info;
  struct node *left;
  struct node *right;
} Node;

Node *insert(Node *h1, int info)
{
  if (!h1)
  {
    h1 = (Node *)malloc(sizeof(Node));
    h1->info = info;
    h1->left = NULL;
    h1->right = NULL;
  }
  else if (h1->info > info)
    h1->left = insert(h1->left, info);
  else
    h1->right = insert(h1->right, info);
  return h1;
}

void bfs(Node *h1)
{
  Node *v;
  queue<Node *> q;

  cout << h1->info;

  q.push(h1->left);
  q.push(h1->right);

  while (!q.empty())
  {
    v = q.front();
    q.pop();
    if (!v)
      continue;

    cout << ' ' << v->info;
    q.push(v->left);
    q.push(v->right);
  }
}

Node *liberate(Node *h1)
{
  if (!h1)
    return NULL;
  h1->left = liberate(h1->left);
  h1->right = liberate(h1->right);
  free(h1);
  return NULL;
}

Node *h;

int main()
{
  int test, n, x;
  int caseNumber = 1;

  cin >> test;
  while (test--)
  {
    h = NULL;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
      cin >> x;
      h = insert(h, x);
    }
    cout << "Case " << caseNumber << ":\n";
    caseNumber++;

    bfs(h);

    if (test == 0)
      cout << "\n";
    else
      cout << "\n\n";

    h = liberate(h);
  }
}