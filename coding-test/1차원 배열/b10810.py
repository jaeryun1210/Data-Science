# 공 넣기
# 바구니 개수: n, 공 넣는 횟수: m
# i번 바구니부터 j번 바구니까지 k번 번호가 적혀져 있는 공을 넣는다


import sys

n,m = map(int, sys.stdin.readline().split())
nlist = [0] * n

for _ in range(m):
    i,j,k = map(int, sys.stdin.readline().split())
    for x in range(i,j+1):
        nlist[x-1] = k

print(*nlist)