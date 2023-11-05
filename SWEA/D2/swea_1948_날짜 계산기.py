T = int(input())
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for test_case in range(1, T+1):
    month1, date1, month2, date2 = map(int, input().split())
    sum = 0
    if month1 == month2:
        sum = date2 - date1 + 1
    else:
        for i in range(month1, month2):
            sum += month[i]
        sum += date2 - date1 + 1
    print(f'#{test_case} {sum}')