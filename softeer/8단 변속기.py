trans = list(map(int, input().split()))
checkDe = [8, 7, 6, 5, 4, 3, 2, 1]
checkAs = sorted(checkDe)
if trans == checkDe:
        print('descending')
elif trans == checkAs:
        print('ascending')
else:
    print('mixed')
