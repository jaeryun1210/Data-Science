# 세 자리 수 a,b 자연수가 주어질 때 곱의 과정 중 값과 최종값을 구하는 프로그램
# 수학, 사칙연산

a = int(input())
b = int(input())

print(a*(b%10))
print(a*(b//10%10))
print(a*(b//100))
print(a*b)

'''
같은 답
a = int(input())
b = input() 2번째 수는 문자열로 받기
for i in [2,1,0]:
    print(a * int(b[i]))
print(a * int(b))
'''