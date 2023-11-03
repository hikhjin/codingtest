import sys
input = sys.stdin.readline

n = int(input())
rocks = list(map(int, input().split()))

# dp 사용
dp = [1] * n

for i in range(1, n):
  for j in range(i):
    if rocks[i] > rocks[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 문제 이해를 잘못해서 해설을 보고 풀긴 했는데 아직도 100퍼센트 이해가 된 것인지 잘 모르겠음..