import sys
input = sys.stdin.readline

cList = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳 리스트
s = input().rstrip() # rstrip: 개행 문자 제거

for i in cList:
    s = s.replace(i, '1') # 크로아티아 알파벳을 1로 치환

print(len(s))