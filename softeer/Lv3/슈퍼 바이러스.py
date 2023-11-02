import sys
input = sys.stdin.readline
virus, p, time = map(int, input().split())

# 재귀 함수로 풀어야 한다!

def cal(i, t):
  if t == 1:
    return i
  elif t % 2 == 0:
    #return (cal(i, t/2) * cal(i, t/2)) % 1000000007
    a = cal(i, t/2) # 이렇게 따로 정의를 하지 않으면 시간 초과로 실패이다!!
    return (a * a) % 1000000007
  else:
    b = cal(i, (t-1) / 2)
    return (b * b * i) % 1000000007
ans = cal(p, 10 * time) * virus
print(ans % 1000000007)

