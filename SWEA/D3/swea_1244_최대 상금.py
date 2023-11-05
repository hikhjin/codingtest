import sys
sys.stdin = open("input_1244.txt", "r")
input = sys.stdin.readline
T = int(input())

for test_case in range(1, T + 1):
    num, n = map(str, input().split())
    # 완전탐색, set 사용하여 중복 제거
    for i in range(n):
        for j in range(i, len(num)):

