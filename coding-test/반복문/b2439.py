# 별찍기-2
# 오른쪽 기준으로 정렬한 별을 n번째 줄에 별 n개찍는 프로그램

n = int(input())
for i in range(n):
    print(" " * (n-i-1) + "*" * (i+1))