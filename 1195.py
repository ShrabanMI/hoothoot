import heapq

inf = 10 ** 18 + 7


def dijkstra(G, s):
    v = len(G) + 1
    par = [-1 for _ in range(v)]
    dis = [inf for _ in range(v)]
    dis[s] = 0

    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        d, u = heapq.heappop(pq)
        if dis[u] < d:
            continue
        for v, w in G[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                par[v] = u
                heapq.heappush(pq, (dis[v], v))

    return dis, par


def createGraph(v, e):
    graph1 = [[] for _ in range(v + 1)]
    graph2 = [[] for _ in range(v + 1)]
    edges = []
    for i in range(e):
        u, v, w = [int(x) for x in input().split()]
        graph1[u].append((v, w))
        graph2[v].append((u, w))
        edges.append((u, v, w))

    return graph1, graph2, edges


def solve():
    n, m = [int(x) for x in input().split()]
    g1, g2, ed = createGraph(m, m)

    dis1, par1 = dijkstra(g1, 1)
    dis2, par2 = dijkstra(g2, n)

    ans = inf
    for a, b, w in ed:
        ans = min(ans, dis1[a] + dis2[b] + w//2)
    print(ans)


solve()