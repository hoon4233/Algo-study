import sys
input = sys.stdin.readline

def dfs(st):
    if st>= n :
        return 0
    if dp[st]!=-1:
        return dp[st]
    dp[st] = max(meet[st][2] + dfs(st+2),meet[st][2] + dfs(st+3))
    return  dp[st]


n = int(input())
dp = [-1 for _ in range(n)]
meet = []
for _ in range(n):
    st, ed, people = map(int,input().split())
    meet.append([st,ed,people])
print(max(dfs(0),dfs(1)))
