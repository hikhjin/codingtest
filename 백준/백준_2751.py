num = int(input())
nums = []
for i in range(num):
    nums.append(int(input()))

for j in sorted(nums): # 오름차순으로 정렬
    print(j)
