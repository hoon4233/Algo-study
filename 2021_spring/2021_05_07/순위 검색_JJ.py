from bisect import bisect_left

d = {}

def solution(info, query):
    answer = []

    # 각 지원자 dfs 수행
    for idx in range(len(info)):
        i = info[idx].split()
        dfs('',i,0)
    
    # 각 key들에 저장되어 있는 코딩 테스트 점수들 정렬
    for key in d:
        d[key] = sorted(d[key])
    
    # 쿼리 처리
    for idx in range(len(query)):
        i = query[idx].split(' and ')
        tmp = i[3].split()
        i[3] = tmp[0]
        val = int(tmp[1])
        q = "".join(i)
        if q in d:
            # 이진탐색으로 idx를 찾아서 점수 조건에 부합하는 사람수를 구함
            answer.append(len(d[q]) - bisect_left(d[q],val))
        else :
            answer.append(0)   
    return answer

def dfs(key,info,cnt):
    # 마지막 조건일 때
    if cnt == 4:
        # 딕셔너리에 저장
        if not key in d:
            d[key] = []
        d[key].append(int(info[4]))
    else :
        dfs(key+'-',info,cnt+1)
        dfs(key+info[cnt],info,cnt+1)