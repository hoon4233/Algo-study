import sys 
import heapq

input = sys.stdin.readline

n,k = map(int,input().split())

bosuks = []
bag = []

# 보석 정보
for idx in range(n):
    m,v = map(int,input().split())
    heapq.heappush(bosuks,[m,v])

# 가방 정보
for _ in range(k):
    bag.append(int(input()))

# 작은거 부터
bag = sorted(bag)
ans = 0
pq = []

for c in bag:

    # 가능한 보석들
    while bosuks:

        # 보석보다 가방이 작을 때
        if bosuks[0][0] > c:
            break
        
        m,v =  heapq.heappop(bosuks)
        # 현재 가방 크기에서 넣을 수 있는 모든 보석이 들어감
        heapq.heappush(pq,-v)
    
    # 넣을 수 있는 보석중에 가장 가치가 높은거 선택
    if pq:
        v =  - heapq.heappop(pq)
        ans = ans + v

print(ans)


