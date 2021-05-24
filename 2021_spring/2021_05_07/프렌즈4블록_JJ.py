def solution(m, n, board):
    answer = 0

    # 회전
    newboard = rotate90(m,n,board)
    
    while 1:
        # 사라지는 블럭이 있는지
        flag = False 

        # 사라질 블럭 체크하는 테이블
        check = [ [True for _ in range(m)] for _ in range(n)]

        for r in range(n-1):
            for c in range(m-1):
                # 2*2 블럭 찾은 경우
                if newboard[r][c] != '*' and newboard[r][c] == newboard[r+1][c] == newboard[r][c+1] == newboard[r+1][c+1]:
                    # 사라질 블럭 체크
                    check[r][c] = check[r+1][c] = check[r][c+1] = check[r+1][c+1] = False
                    flag = True
        
        for r in range(n):
            # 블럭 사라진 뒤에 로우 구하기
            newRow = ['*' for _ in range(m)]
            idx = 0
            # 왼쪽부터 채워 나감 -> 90도 돌려서 가능
            for c in range(m):
                if check[r][c]:
                    newRow[idx] = newboard[r][c]
                    idx = idx + 1
                else : 
                    # 사라지는 블럭 합산
                    answer = answer + 1
                    
            newboard[r] = newRow
        
        # 하나도 안사라지는 경우 break
        if not flag :
            break
            
    return answer


def rotate90(row,columm,board): 
    ret = [[0] * row for _ in range(columm)] 
    for r in range(row): 
        for c in range(columm):
            ret[c][row-1-r] = board[r][c]   
    return ret

def printTable(board):
    for i in board:
        for j in i:
            print(j,end='')
        print('')

print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))
print(solution(4 , 5, ["AAAAA","AUUUA","AUUAA","AAAAA"] ))
print(solution(6 , 6, ["AABBFF","AAAFFF","VAAFFV","AABBFF","AACCFF","VVCCFF" ] ))
