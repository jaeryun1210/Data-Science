# 최소, 최대
# n개의 정수가 주어지면 최솟값과 최댓값을 구하는 프로그램

import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

print(min(l),max(l))