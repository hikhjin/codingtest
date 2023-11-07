import sys
input = sys.stdin.readline

size, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True) # 큰 수대로 정렬
max1 = l[0] # 첫번쨰로 큰 수
max2 = l[1] # 두번쨰로 큰 수
ans = 0
isLim = 0 # k 넘었는지 확인
while m != 0:
    if isLim == 1:
        ans += max2
        m -= 1
        isLim = 0
    elif isLim == 0 and m < k:
        ans += max1 * m
        break
    else:
        if m % k == 0:
           isLim = 1
        ans += max1
        m -= 1
print(ans)
