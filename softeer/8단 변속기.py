trans = list(map(int, input().split()))
checkDe = [8, 7, 6, 5, 4, 3, 2, 1]
checkAs = sorted(checkDe)
for i in range(8):
    if trans == checkDe:
        print('descending')
        break
    elif trans == checkAs:
        print('ascending')
        break
    else:
        print('mixed')
        break