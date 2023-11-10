import sys
input = sys.stdin.readline

arr = [[0] * 100 for i in range(100)] # 전체 넗이
p = int(input())

for _ in range(p):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1
ans = 0
for i in range(100):
    ans += arr[i].count(1)

print(ans)