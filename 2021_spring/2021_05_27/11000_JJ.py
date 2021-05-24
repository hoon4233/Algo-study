import sys
import heapq

input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    s,t = map(int,input().split())
    data.append([s,t])

data = sorted(data)

# 힙에 끝나는 시간만 기록
pq = [data[0][1]]
ans = len(pq)

for i in range(1,len(data)):
    st, ed = data[i][0],data[i][1]
    if pq[0] <= st:
        heapq.heappop(pq)
        heapq.heappush(pq,ed)
    else :
        heapq.heappush(pq,ed)
        ans = max(ans,len(pq))
print(ans)