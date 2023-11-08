import sys
input = sys.stdin.readline

while 1:
    num = str(input()).rstrip()
    if num == '0':
        break
    check = 0 # 펠린드롬인지 확인
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            check = 1
            break

    if check == 1:
        print("no")
    else:
        print("yes")