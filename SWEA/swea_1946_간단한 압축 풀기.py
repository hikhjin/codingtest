import sys
sys.stdin = open("input_1206.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    cnt = int(input()) # 문자 수
    print(f'#{test_case}')
    ans = []
    for i in range(cnt):
        word, num = map(str, input().split()) # 일단 문자형으로 문자와 반복 수 받기
        for j in range(int(num)): # num 만큼 문자 반복
            ans.append(word) # 10개로 끊지 않은 초기 리스트 생성
    isTen = 0 # 줄바꿈 해야 하는지 확인
    for k in range(len(ans)):
        if ((k+1) % 10 == 0) or (k+1) == len(ans): # 줄바꿈을 해야 하는 경우(마지막 줄 포함)
            if (k+1) == 1: # 인덱스 0 제외
                print(ans[k], sep='', end='')
            else:
                print(ans[k], sep='', end='\n')
        else:
            print(ans[k], sep='', end='')

