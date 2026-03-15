# 바구니 뒤집기

import sys

n,m = map(int, sys.stdin.readline().split())
nlist = list(range(1,n+1))

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    
    while i < j:
        nlist[i-1], nlist[j-1] = nlist[j-1], nlist[i-1]
        i += 1
        j -= 1

print(*nlist)