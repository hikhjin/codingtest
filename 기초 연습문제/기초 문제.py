# 각 자리 숫자 합 구하기 (map)
def sumOfDigits_map(num):
    digit = list(map(int, str(num)))
    print(digit)
    return sum(digit)


# 펠린드롬인지 확인
def isPalindrome(word):
    word = word.lower()
    word = word.replace(' ', '')
    return word[:] == word[::-1]


# print(isPalindrome('My Gym'))

# 각 자리 숫자 합 구하기(list)
def sumOfDigits_list(num):
    sum = 0
    num = list(str(num))
    # print(num)
    for i in num:
        # print(i)
        sum += int(i)
    return sum


# print(sumOfDigits_list(643))

# 이진법 변환
def deToBi():
    decimal = int(input('십진수: '))
    binary = list(bin(decimal))
    binary.remove('b')
    binary.remove('0')
    print(binary)


# deToBi()

# 내일의 날짜 구하기
def read_date():
    year, month, date = tuple(map(int, input('입력: ').split(' ')))
    return year, month, date


def print_day(day):
    year, month, date = day
    print(f'{month}/{date}/{year}')


def tomorrow(day):
    year, month, date = day
    end_of_month = (month, date) in [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31),
                                     (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    end_of_year = (month, date) in (12, 31)

    if end_of_month:
        if end_of_year:
            year += 1
            month = 1
            date = 1
        else:
            month += 1
            date = 1
    else:
        date += 1
    return year, month, date

# 한국어 숫자 출력
def koreanNum(num):
    korean = {1: '일', 2: '이', 3: '삼', 4: '사'}
    print(korean[num])

