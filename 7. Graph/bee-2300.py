def connected(graph_transformers, start_station):
    nvertices = len(graph_transformers)

    status = [0] * nvertices
    fifo = [start_station]
    status[start_station] = 1

    while fifo != [] and 0 in status:
        v = fifo.pop()
        for w in range(nvertices):
            if graph_transformers[v][w] == 1 and status[w] == 0:
                status[w] = 1
                fifo.append(w)
    return 0 not in status


nodes, edges = map(int, input().split())
test = 0
while nodes + edges != 0:
    test += 1
    graph_transformers = [[0]*nodes for k in range(nodes)]
    for i in range(edges):
        x, y = map(int, input().split())
        graph_transformers[x-1][y-1] = 1
        graph_transformers[y-1][x-1] = 1
    print(f"Teste {test}")
    print("normal\n" if connected(graph_transformers, 1) else "falha\n")
    nodes, edges = map(int, input().split())
