
import sys
sys.stdin = open("input_1206.txt", "r")
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cnt = int(input()) # 건물 개수
    height = list(map(int, input().split())) # 건물 높이 리스트로 받기
    ans = 0 # 조망권 확보된 세대 개수
    for i in range(2, cnt-2):
        max_height = max(height[i-1], height[i-2], height[i+1], height[i+2])
        if height[i] > max_height:
            ans += height[i] - max_height
    print(f'#{test_case} {ans}')


