'''
거스름돈으로 사용할 500원, 100원, 50원, 10원을 가지고 거슬러 줘야 할 동전의 최소 개수를 구해라.
'''
# 그리디 알고리즘

import sys
input = sys.stdin.readline

t = int(input()) # 입력 받는 금액
coins = [500, 100, 50, 10]
cnt = 0

for coin in coins:
    cnt += (t // coin) # //: 나눈 몫을 정수로 나타냄
    t %= coin
print(cnt)