# 나머지
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구하고
# 서로 다른 값이 몇 개 있는지 출력하는 프로그램

import sys

nlist = []

for _ in range(10):
    n = int(sys.stdin.readline())
    nlist.append(n%42)

print(len(set(nlist)))
