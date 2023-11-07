import sys
sys.stdin = open("input_1209.txt", "r")

T = 10
for test_case in range(1, T + 1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    temp_c1 = 0
    temp_c2 = 0

    temp_r = [sum(arr[i]) for i in range(100)]  # 각 열 합 리스트
    max_r = max(temp_r) # 열의 최댓값

    for i in range(100): # 대각선
        temp_c1 += arr[i][i] # 좌측에서 시작하는 대각선
        temp_c2 += arr[99-i][i] # 우측에서 시작하는 대각선
    max_c = max(temp_c1, temp_c2) # 대각선의 최댓값

    temp_col = [0]*100
    for i in range(100):
        for j in range(100):
            temp_col[i] += arr[j][i]
    max_col = max(temp_col) # 행의 최댓값

    print(f'#{t} {max(max_r, max_col, max_c)}')

