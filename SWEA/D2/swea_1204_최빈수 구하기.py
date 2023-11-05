import sys
from collections import Counter

sys.stdin = open("input_1204.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    testNum = int(input()) # 테스트케이스 넘버
    scoreList = list(map(int, input().split())) # 각 점수 리스트로 받기
    modeCnt = Counter(scoreList) # 카운터 모듈을 이용하여 딕셔너리 형태로 각 점수 별로 빈도수 저장
    modeList = [x for x, y in modeCnt.items() if max(modeCnt.values()) == y] # 리스트 컴프리헨션을 사용하여 최빈값 리스트 생성
    ans = max(modeList)
    print(f'#{testNum} {ans}')
