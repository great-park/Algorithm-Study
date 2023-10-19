import heapq as hq
V,E = map(int, input().split())
visited = [False] * (V + 1)
edges = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    edges[s].append([w, e])
    edges[e].append([w, s])

heap = [[0,1]]
answer = 0
cnt = 0

while heap:
    if cnt == V:
        break
    w, s = hq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for edge in edges[s]:
            hq.heappush(heap, edge)

print(answer)

# 2. 크루스칼 알고리즘

# V, E = map(int, input().split())
# edges = [list(map(int, input().split())) for _ in range(E)]
# edges.sort(key=lambda x: x[2])
# parent = [i for i in range(V+1)]
#
# def get_parent(x):
#     if parent[x] == x:
#         return x
#     parent[x] = get_parent(parent[x])
#     return parent[x]
#
# def union_parent(a, b):
#     a = get_parent(a)
#     b = get_parent(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# answer = 0
# for a, b, cost in edges:
#     if get_parent(a) != get_parent(b):
#         union_parent(a, b)
#         answer += cost
# print(answer)