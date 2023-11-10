import sys
input = sys.stdin.readline

n = int(input())
cnt = 0 # 몇번째인지 체크
ans = 0

while cnt <= n:
    if '666' in str(ans): # 수 안에 666이 있으면 cnt 증가
        cnt += 1
    if cnt == n: # n과 같으면 1 더하지 않고 나감
        break
    ans += 1

print(ans)