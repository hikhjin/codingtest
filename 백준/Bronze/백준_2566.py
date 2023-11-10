import sys
input = sys.stdin.readline

nums = [list(map(int, input().split())) for _ in range(9)]
m = 0
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if m <= nums[i][j]:
            m = nums[i][j]
            x = i + 1
            y = j + 1
print(m)
print(x, y)