import sys
sys.stdin = open("input_1208.txt", "r")
T = 10

for test_case in range(1, T + 1):
    count = int(input())
    height = list(map(int, input().split()))

    for i in range(count):
        if max(height) - min(height) == 0 or max(height) - min(height) == 1:
            break
        height[height.index(max(height))] -= 1
        height[height.index(min(height))] += 1
    ans = max(height) - min(height)

    print(f'#{test_case} {ans}')