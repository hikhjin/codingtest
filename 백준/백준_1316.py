num = int(input())
#word = [str(input()) for i in range(num)] # num 만큼 입력 받기

for i in range(num):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]:
            num -= 1
            break
print(num)

