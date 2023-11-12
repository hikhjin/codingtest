import sys
input = sys.stdin.readline

b = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
w = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
chessB = []
chessW = []
for i in range(8): # 정답 체스판
    if i % 2 == 0:
        chessB.append(b)
        chessW.append(w)
    else:
        chessB.append(w)
        chessW.append(b)

check = set() # 바꿔야 할 개수 집합

n, m = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(8)] # 입력 받은 보드

for i in range(0, n-8):
    for j in range(0, m-8):
        cnt1 = 0  # chessB와 비교할 때 개수 세기
        cnt2 = 0  # chessW와 비교할 때 개수 세기
        for k in range(8):
            print(i+k, j+k)
            print(board[i+k][j+k])
            print(chessB[i+k][j+k])
            print(chessW[i+k][j+k])
            if board[i+k][j+k] != chessB[i+k][j+k]: # 체스판과 값이 다를 경우 cnt 증가
                cnt1 += 1
            if board[i+k][j+k] != chessW[i+k][j+k]:
                cnt2 += 1
        check.add(cnt1)
        check.add(cnt2)
        print(cnt1, cnt2)
print(check)
print(min(check))



