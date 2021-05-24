import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
d = sorted(data)

idxF,idxR = 0, n-1
ansF,ansR = 0, n-1
mind = 2000000001

while idxF<idxR:
    nowd = d[idxF] + d[idxR]
    posnowd = abs(d[idxF] + d[idxR])

    # 더욱 작을 때
    if posnowd < mind:
        mind = posnowd
        ansF,ansR = idxF,idxR

    # 음수이면 앞의 포인터 이동
    if nowd < 0:
        idxF = idxF + 1
    # 양수이면 뒤에 포인터 이동
    else :
        idxR = idxR - 1

print(d[ansF],d[ansR])




