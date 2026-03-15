# 최댓값
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고
# 그 최댓값이 몇 번째 수인지 구하는 프로그램

nlist = []

for _ in range(9):
    n = int(input())
    nlist.append(n)

print(max(nlist))
print(nlist.index(max(nlist))+1)

'''
for i in range(9):
    a = int(input())
    if i == 0:
        maxn = a
        cnt = i+1
    elif maxn < a:
        maxn = a
        cnt = i+1

print(maxn)
print(cnt)
'''