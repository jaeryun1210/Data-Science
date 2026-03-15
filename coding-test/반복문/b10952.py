# 두 정수 a,b 입력받고 a+b 출력하는 프로그램
# 0 0을 마지막으로 반복하는 프로그램

import sys

while(1):
    a,b = map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    else:
        print(a+b)