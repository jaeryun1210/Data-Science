# 알람 시각이 주어졌을 때 45분 앞선 시간으로 고치는 프로그램
# 수학,사칙연산
# 0<=H<=23, 0<=M<=59
H,M = map(int, input().split())
if M-45<0:
    H = H-1
    M = M+15
    if H<0:
        H = 23
else:
    M = M-45
print(H,M)