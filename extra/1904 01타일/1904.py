import time
import sys
start = time.time()
d=[0]*1000001
d[1] = 1
d[2] = 2

N = int(sys.stdin.readline())
for i in range(3,N+1):
    d[i] = (d[i-1]%15746+d[i-2]%15746)%15746
print(d[N])
print(time.time() - start)
