# 개수 세기
# n개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램
'''
# 문자로 비교
n = input()
arr = input().split()
v = input()
print(arr.count(v))
'''
'''
남의 코드
N = int(input())
A = list(map(int, input().split(' ')))
v = int(input())

count = 0

for i in range(len(A)):
    if A[i] == v: count += 1

print(count)
'''

'''
숫자로 비교
n = int(input())
arr = list(map(int, input().split()))
v = int(input())
print(arr.count(v))
'''

'''
readline 버전(문자)
import sys

n = sys.stdin.readline().strip()
arr = sys.stdin.readline().split()
v = sys.stdin.readline().strip()

print(arr.count(v))
'''


# readline버전(숫자)
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(arr.count(v))
