# 평균
# 성적을 새로 계산해서 평균을 구하는 프로그램
# 자기 점수 중 최댓값 m, 모든 점수를 점수/m*100

import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
a = 0
for i in range(n):
    a += (s[i] / max(s)) * 100
    
print(a/n)