lim, tes = map(int, input().split())
limit = [list(map(int, input().split())) for _ in range(lim)]
test = [list(map(int, input().split())) for _ in range(tes)]

speed_limit = []
speed_test = []

for length, speed in limit:
    speed_limit += [speed for i in range(length)] # 배열로 제한 속도 저장

for length, speed in test:
    speed_test += [speed for i in range(length)] # 배열로 test 속도 저장

overSpeed = [speed_test[i] - speed_limit[i] for i in range(100)]
if max(overSpeed) < 0: # 음수일 경우 0
    print('0')
else:
    print(max(overSpeed))