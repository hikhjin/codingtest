sec, user, but = map(int, input().split())
sCode = str(input().replace(' ', '')) # 문자열로 비밀 메뉴 코드 받기
uCode = str(input().replace(' ', '')) # 문자열로 사용자가 입력한 코드 받기
if sCode in uCode:
    print('secret')
else:
    print('normal')