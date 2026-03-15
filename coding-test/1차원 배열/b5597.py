# 과제 안 내신 분..?
# 1번부터 30번 중 과제 제출 안 한 학생 2명의 출석번호를 구하는 프로그램

nlist = list(range(1,31))

for _ in range(28):
    n = int(input())
    nlist.remove(n)

print(min(nlist))
print(max(nlist))