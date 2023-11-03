import sys
input = sys.stdin.readline
'''
n = int(input())
lecs = [list(map(int, input().split())) for _ in range(n)]

ans = 0
check = [0] * 24 # 시간 확인용 배열

for i in range(n):
  if check[lecs[i][0]] == 0 or (check[lecs[i][0]] == 1 and check[lecs[i][0]+1] == 0):
    ans += 1
    for j in range(lecs[i][0], lecs[i][1]+1):
      if check[j] == 1 and check[j+1] == 1:
        ans -= 1
        break
      check[j] = 1

print(ans)'''

# 실패

import heapq

n = int(input())

ans = 0

# 힙큐 사용한다. (정렬 필요하기 때문)
heap = []
for _ in range(n):
  start, finish = map(int, input().split())
  heapq.heappush(heap, (finish, start)) # 힙큐에 하나씩 넣어줌, finish 기준으로 정렬하기 위해 앞에 넣음

current = 0
while heap: # heap에 아무것도 없을 때까지 반복
  finish, start = heapq.heappop(heap)
  if start >= current: # (시작시간과 종료시간은 겹쳐도 되므로 >= 사용) 기준점보다 시작시간이 느리면
    current = finish # 기준점을 finish로 바꾸기
    ans += 1
print(ans)
