import sys
input = sys.stdin.readline

grades = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
c_List = [] # 수강 학점 수 리스트
g_List = [] # 받은 성적 리스트

for _ in range(20):
    n, c, g = input().split()
    c_List.append(float(c))
    g_List.append(g)

total_c = sum(c_List) # 총 수강 학점 수
total_g = 0.0 # 총 성적 합

for i in range(len(g_List)):
    if g_List[i] == 'P': # P이면 계산 제외이므로 총 학점에서 빼줌
        total_c -= c_List[i]
        continue
    total_g += grades.get(g_List[i]) * c_List[i] # 받은 성적 * 수강 학점

print(total_g / total_c)
