import sys     #왜 런타임 오류 나는지 모르겠습니다...
sys.setrecursionlimit(10**8)
def dfs(t):
    global result
    for i in range(N):
        while adj[t][i] :
            if adj[t][i] > 0:
                adj[t][i] -= 1
                adj[i][t] -= 1
                dfs(i)
    print(t+1, end = " ")
    # result.append(t+1)


N = int(input())
adj=[]
for i in range(N):
    adj.append(list(map(int,sys.stdin.readline().rstrip().split())))
# adj = [ list(map(int,input().split())) for _ in range(N) ]
flag = False
s = [0 for _ in range(N)]
result = []

# for i in range(N):
#     if(sum(adj[i])%2 == 1 ):
#         flag = True
#         break


for i in range(N):
    for j in range(N):
        s[i] += adj[i][j]
    if s[i]%2 == 1 :
        flag = True
        break
        


if flag :
    print(-1)
else :
    dfs(0)
    # print(*result[::-1])
    # for i in result[::-1]:
    #     print(i, end = " ")
    # result.reverse()
    # print(*result)


# import sys
# sys.setrecursionlimit(10**9)

# N=int(input())
# L=[]
# for i in range(N):
#     L.append(list(map(int,sys.stdin.readline().rstrip().split())))

# edge=0
# graph={}
# for i in range(N):
#     graph[i]=[]
#     rowSum=0
#     for j in range(N):
#         for _ in range(L[i][j]):
#             rowSum+=1
#             graph[i].append(j)
#     if rowSum%2==1:
#         print(-1)
#         sys.exit()
#     else:
#         edge+=rowSum
# edge=edge//2
# print(graph)

# def dfs(nowNode):
#     for conNode in graph[nowNode]:
#         if L[nowNode][conNode]:
#             L[nowNode][conNode]-=1
#             L[conNode][nowNode]-=1
#             dfs(conNode)
#     print(nowNode+1,end=" ")

# dfs(0)