import sys

nCnt, mCnt = map(int, input().split())  # 회의실 수: nCnt, 회의 수: mCnt
name = [str(sys.stdin.readline().rstrip()) for _ in range(nCnt)]
meetings = [[0 for _ in range(10)] for _ in range(nCnt)]  # 2차원 배열 선언, 맨 첫 칸은 회의실 이름
name.sort()  # 이름 오름차순 정렬

for i in range(nCnt):  # 첫 칸에 회의실 이름 저장
    meetings[i][0] = name[i]


def meetingRoom(room, start, end):
    for i in range(nCnt):
        if room == meetings[i][0]:  # 해당 회의실 리스트에서
            for j in range(start, end):
                meetings[i][j - 8] = 1  # 예약된 시간을 1로 바꿈, 시작 시간이 9시니까 8 빼줌


for _ in range(mCnt):
    meetInfo = list(map(str, input().split()))
    meetingRoom(meetInfo[0], int(meetInfo[1]), int(meetInfo[2]))


def appendZero(nList):  # 한 자리수에 0 붙이기
    for i in range(len(nList)):
        if len(nList[i]) == 1:
            nList[i] += '0'


print(meetings)

for i in range(nCnt):
    start = 0
    end = 0
    isStart = 1  # start인지 확인
    times = []
    if 0 not in meetings[i]:  # 비는 시간이 없을 경우
        print('Not available')
    else:
        for j in range(1, 10):
            if isStart == 1:
                start = j + 8
                end = j + 8
                isStart = 0
            else:
                end = j + 8
                if meetings[i][j] == 1:
                    isStart = 1
                    times.append([start, end])
    print(times)

    if i != nCnt:  # 마지막 아닐 때만 바 출력
        print('-----')
