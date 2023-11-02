import sys
n, k = list(map(int, sys.stdin.readline().split()))
grade = list(map(int, sys.stdin.readline().split()))

for i in range(k):
  s1, s2 = list(map(int, sys.stdin.readline().split()))
  ans = 0
  for j in range(s1, s2 + 1):
    ans += grade[j-1]
  ans = round(ans/(s2-s1+1), 2)
  print(ans)

