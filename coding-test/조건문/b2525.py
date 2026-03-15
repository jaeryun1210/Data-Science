# 시작하는 시각과 하는 데 필요한 시간이 분단위로 주어졌을 때, 끝나는 시각을 계산하는 프로그래매
# 수학,사칙연산
#현재시각 A시(0<=A<=23) B분(0<=B<=59)
A,B = map(int, input().split())
#필요한 시간 C분(0<=C<=1000)
C = int(input())

if B+C<60:
    B += C
elif (B+C)%60==0:
    A = A+(B+C)//60
    if A==24:
        A = 0
    elif A>24:
        A = A%24
    B = 0
else:
    A = A+(B+C)//60
    if A==24:
        A = 0
    elif A>24:
        A = A%24
    B = (B+C)%60
print(A,B)