import sys
input = sys.stdin.readline

def getP(x):
    if p[x] == x :
        return x
    p[x] = getP(p[x])
    return p[x]

def merge(a,b):
    pa = getP(a)
    pb = getP(b)
    if pa==pb:
        return False
    else :
        p[pb] = pa
        return True

n,m = map(int,input().split())
edges = []
ans = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append([c,a-1,b-1])
    ans = max(ans,c)

st, ed =  map(int,input().split())
st, ed = st-1, ed-1
p = [i for i in range(n)]

# 엣지 정렬
edges = sorted(edges, reverse=True)
ans = 0
for [c,a,b] in edges:
    
    # 합쳐졌을때
    if merge(a,b):
        if getP(st) == getP(ed):
            ans = c
            break

print(ans)