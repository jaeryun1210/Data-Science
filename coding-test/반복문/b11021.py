# a+b-7
# 두 정수 a,b 입력받은 다음, a+b를 출력하는 프로그램
# 각 테스트 케이스마다 Case #x:를 출력 후 a+b 출력
# 수학,구현,사칙연산
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print(f"Case #{i+1}: {a+b}")