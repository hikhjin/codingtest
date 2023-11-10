import sys
input = sys.stdin.readline

arr = [list(str(input().rstrip())) for _ in range(5)]
length = max(len(s) for s in arr) # 문자열 길이 최댓값

ans = ''
for i in range(len(arr)):
    if len(arr[i]) < length: # 최대 길이보다 짧을 경우 '' 추가
        for j in range(length-len(arr[i])):
            arr[i].append('')

for i in range(length):
    for j in range(len(arr)):
        ans += arr[j][i]
print(ans)