import sys

imput = sys.stdin.readline

def gcd(a,b):
  if b==0 :
    return a
  return gcd(b,a%b)

def solve():

  m = int(input())
  allgcd = 0
  
  moneys = []
  lefts = []
  beforeLeft = 0

  for i in range(m):
    money,left = map(int,input().split())

    # 데이터 저장
    moneys.append(money)
    lefts.append(left)

    # 출금일 때
    if money < 0 :
      chargedMoney = left - money - beforeLeft
    
      # 실제 충전이 되었을 때
      if chargedMoney > 0:

        # 최대공약수 업데이트
        allgcd = gcd(chargedMoney,allgcd)

    beforeLeft = left

  if allgcd == 0:
    allgcd = 1

  beforeLeft = 0
  for i in range(m):

    # 입금일때
    if moneys[i] >= 0:

      # 입금 후 금액이 일치하지 않는다면
      if beforeLeft + moneys[i] != lefts[i]:
        return -1

    # 출금일때 
    else :
      
      # 충전이 필요없을 때
      if -moneys[i] <= beforeLeft :

        # 출금 후 금액이 일치하지 않는다면
        if beforeLeft + moneys[i] != lefts[i]:
          return -1

      # 충전 필요할 때
      else :
        # 구한 gcd값(충전최소금액) 보다 잔액이 더 많은 경우
        if allgcd <= lefts[i]:
          return -1

    beforeLeft = lefts[i]

  return allgcd

print(solve())