def solution(key, lock):
    m,n = len(key),len(lock)

    # 자물쇠 테이블에서 홈 저장 - lock[i][j]=0 일 때 [i,j] 저장 
    homes = getlockList(lock)

    # 회전
    for _ in range(4):
        key = rotate90(m,m,key)

        # 축이동 -> lock이 가운데 있고 key table을 왼쪽 상단부터 겹쳐나갈 예정
        for rowMove in range(-m+1,n):
            for colummMove in  range(-m+1,n):

                keys = []
                for row in range(m):
                    for columm in range(m):
                        m_row = rowMove + row
                        m_columm = colummMove + columm

                        # 범위 안일 때 - lock과 겹치는 부분만
                        if is_in(m_row,m_columm,n):
                            # key에서 1인 부분 저장
                            if key[row][columm] == 1:
                                keys.append([m_row,m_columm])
                # 저장해놓은 key table에 1인 좌표들과 
                # lock table에 0인 좌표들이 같을 때 
                if homes == keys :
                    return True
    return False

def is_in(x,y,n):
    return 0<=x<n and 0<=y<n

def rotate90(row,columm,board): 
    ret = [[0] * row for _ in range(columm)] 
    for r in range(row): 
        for c in range(columm):
            ret[c][row-1-r] = board[r][c]   
    return ret

def getlockList(lock):
    n = len(lock)
    ret = []
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                ret.append([i,j])
    return ret