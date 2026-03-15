# 공 바꾸기
# 공 위치 바꾸는 프로그램
n,m = map(int, input().split())
nlist = list(range(1,n+1))
k = 0
for _ in range(m):
    i,j = map(int, input().split())
    k = nlist[i-1]
    nlist[i-1] = nlist[j-1]
    nlist[j-1] = k

    # baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(*nlist)