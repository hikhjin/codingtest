virus, rate, time = map(int, input().split())
for i in range(time):
    virus = (virus * rate) % 1000000007 # 모듈러 연산, 나머지들 간의 연산은 전체 연산의 나머지와 같다. -> 미리 나머지를 계산해두어도 됨.
print(virus)
# 연산이 끝난 후 나머지를 구하면 시간초과로 실패