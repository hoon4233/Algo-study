import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = defaultdict(dict)

for _ in range(m):
    a,b = map(int,input().split())
    adj[a][b] = True
    adj[b][a] = True


visited = [False for _ in range(n+1)]
visited[1] = True
q = deque([1])
dis = 0
ans = 0
while q:
    sz = len(q)
    for _ in range(sz):
        now = q.popleft()
        for key in adj[now].keys():
            if not visited[key] and dis<2:
                q.append(key)
                visited[key] = True
                ans = ans + 1
    dis = dis + 1
print(ans)
