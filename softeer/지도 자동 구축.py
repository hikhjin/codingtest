step = int(input())
ans = 0
sList = []
for i in range(step):
    sList.append(2**(step-1)) # 2 + 2 ** (step-1) + 2 ** (step-2) ...
    step -= 1
    if step == 0:
        break
ans = (2 + sum(sList)) ** 2
print(ans)