# 빠른 a+b
# 첫 줄에 테스트케이스 개수 t(최대 백)
# 다음 t줄에 두 정수 a,b가 주어지고 a+b 출력하는 프로그램

import sys
input = sys.stdin.readline

# t = int(sys.stdin.readline().rstrip())
t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print(a+b)