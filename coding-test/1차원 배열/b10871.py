# x보다 작은 수
# 정수 n개로 이루어진 수열 a와 정수 x가 주어짐
# a에서 x보다 작은 수를 모두 출력하는 프로그램

import sys
input = sys.stdin.readline

n,x = map(int, input().split())
a = list(map(int, input().split()))
l1 = ""
for i in range(n):
    if a[i] < x:
        l1 += str(a[i]) + " "
print(l1)

'''
N, X = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(N):
    if int(lst[i]) < X:
        print(lst[i])
    else:
        pass
'''