import heapq as pq
inf = 10**6+10

def dijkstra(G, s, d):
    dis = {key: inf for key in G}
    parents = {key: key for key in G}
    dis[s] = 0

    q = []
    pq.heappush(q, (0, s))
    while q:
        d, u = pq.heappop(q)
        if d > dis[u]:
            continue
        for v, w in G[u]:
            if dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                parents[v] = u
                pq.heappush(q, (dis[v], v))
    return dis, parents


def createGraph():
    n, m = [int(x) for x in input().split()]
    graph = {i: [] for i in range(1, n+1)}
    for i in range(m):
        u, v, w = [int(x) for x in input().split()]
        graph[u].append((v, w))
        graph[v].append((u, w))
    s, d = 1, n
    return graph, s, d


def routeTrack(parents, d):
    route = [d]
    while d != 1:
        route.append(parents[d])
        d = parents[d]
    return route[::-1]


def solve():
    graph, source, dest = createGraph()
    distances, parents = dijkstra(graph, source, dest)

    route = routeTrack(parents, dest)

    print(*route)


solve()