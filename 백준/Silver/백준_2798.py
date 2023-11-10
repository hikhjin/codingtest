import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

s = set() # 합 저장할 set

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > m: # M 넘으면 저장하지 않음
                continue
            s.add(cards[i] + cards[j] + cards[k]) # 모든 조합 저장
print(max(s))