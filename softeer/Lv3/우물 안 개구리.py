import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memInfo = list(map(int, input().split()))
friend = [list(map(int, input().split())) for _ in range(m)]
temp = [1] * n # 자신이 최고라고 생각하는 회원 상태: 1

for i in range(m):
    if memInfo[friend[i][0] - 1] > memInfo[friend[i][1] - 1]:
        temp[friend[i][1] - 1] = 0
    elif memInfo[friend[i][0] - 1] < memInfo[friend[i][1] - 1]:
        temp[friend[i][0] - 1] = 0
    else:  # 같은 무게를 들 수 있으면 둘 다 0
        temp[friend[i][0] - 1] = 0
        temp[friend[i][1] - 1] = 0

print(temp.count(1))