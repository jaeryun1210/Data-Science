# a+b-8
# 두 정수 a,b 입력받고 a+b 출력하는 프로그램
# Case #x: a+b=c 형식으로 출력

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")
