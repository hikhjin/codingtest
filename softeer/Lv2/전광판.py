import sys
T = int(input()) # 테스트 케이스 개수

# 켜져있으면 1, 꺼져있으면 0 / 처음에 리스트로 했다가 문자열로 바꿔서 수정
zero = '1011111'
one = '0000011'
two = '1110110'
three = '1110011'
four = '0101011'
five = '1111001'
six = '1111101'
seven = '1001011'
eight = '1111111'
nine = '1111011'

nums = {'0': zero, '1': one, '2': two, '3': three, '4': four, '5': five, '6': six, '7': seven,
        '8': eight, '9': nine, ' ': '0000000'}

for test_case in range(1, T+1):
    num1, num2 = input().split() # 두 수 받기 / 처음에 int으로 받고 다시 str으로 바꾸는 뻘짓을 했다.
    cnt = 0 # 최소 횟수

    num1 = (5-len(num1)) * ' ' + num1 # 5자리로 만들기 / 처음에 for문 + 조건문으로 하는 뻘짓을 했다.
    num2 = (5-len(num2)) * ' ' + num2

    for i in range(5):
        for j in range(7):
            if nums[num1[i]][j] != nums[num2[i]][j]:
                cnt += 1

    print(cnt)