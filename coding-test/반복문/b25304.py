# 영수증
# 구매한 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사하는 프로그램
# 수학,구현,사칙연산

# 영수증에 적힌 총 금액
x = int(input())

#영수증에 적힌 구매한 물건의 종류의 수
n = int(input())

sum1 = 0 # a*b의 합
sum2 = 0 # 총합

# n개의 줄에 각 물건의 가격 a와 개수 b
for i in range(n):
    a,b = map(int, input().split())
    sum1 = a*b
    sum2 += sum1
#계산 금액과 영수증의 금액이 일치하면 yes, 아니면 no 출력
if x==sum2:
    print("Yes")
else:
    print("No")

'''
x = int(input())
n = int(input())

total = 0

for i in range(n):
    a, b = map(int, input().split())
    total += a * b

if x == total:
    print("Yes")
else:
    print("No")

'''