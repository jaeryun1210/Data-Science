# A+B - 3
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
# 수학,구현,사칙연산
t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    print(a+b)