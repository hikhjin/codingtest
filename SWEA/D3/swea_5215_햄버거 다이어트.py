import sys
sys.stdin = open("input_5215.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, l = map(int, input().split())
    score = []
    cal = []
    ham_s = []
    ham_c = []
    for _ in range(n):
        s, c = map(int, input().split())
        score.append(s)
        cal.append(c)
    score.sort(reverse=T)
    cal.sort(reverse=T)
    while cal >= 0:
        i=0
        ham_s.append(score[i])
        cal
