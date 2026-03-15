# 두 정수 A B를 입력받고 A+B를 출력하는 프로그램
# 첫 줄에 A와B(0<A,B<10), 첫 줄에 A+B 출력
# 수학,구현,사칙연산
A, B = map(int, input().split())
print(A+B)

'''
기본(문자열) : a = input() 
여러 문자열 : words = input().split()
숫자 하나 : n = int(input())
여러 숫자 : a, b = map(int, input().split())
리스트 : arr = list(map(int, input().split()))
여러 줄 입력 : 
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
빠른 입력 : 
import sys
input = sys.stdin.readline
n = int(input())

strip() : 문자열 앞,뒤에 붙은 공백, 개행 문자 제거
split() : 문자열 구분자 기준으로 나눠줌(직접 지정 가능)
split의 결과는 리스트, strip은 문자열 전용
같이 쓸 경우 strip가 앞

map(함수, 반복가능한것) : 리스트의 각 원소에 함수를 하나씩 적용
map은 결과를 바로 만들지 않고 하나씩 꺼내 쓰는 형태(이터레이터)라 list()로 감싸줘야됨
'''