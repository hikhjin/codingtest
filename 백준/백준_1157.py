import sys
from collections import Counter
input = sys.stdin.readline

s = input().rstrip().upper() # 대소문자 구분하지 않으므로 대문자로 바꿈
cnt = Counter(s) # 카운터 사용하여 딕셔너리 형태로 각 글자 수 받음
max_count = max(cnt.values()) # 가장 많이 나온 알파벳의 개수
max_count_letters = [letter for letter, count in cnt.items() if count == max_count] # 가장 많이 나온 알파벳의 개수와 같을 때만 알파벳을 리스트에 저장

if len(max_count_letters) == 1: # 최대 개수 알파벳이 하나면
    print(max_count_letters[0])
else: # 여러개면
    print('?')