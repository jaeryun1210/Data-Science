# 숫자의 합
# n개의 숫자가 공백없이 주어졌을 때, 모두 합해서 출력하는 프로그램

import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().rstrip()))
s = 0
for i in range(n):
    s += nlist[i]

print(s)

'''
rstrip() : 문자열 오른쪽 끝에서 특정 문자들을 제거하는 함수
기본적으로 공백제거로 사용한다
'''