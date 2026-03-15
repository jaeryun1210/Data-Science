# 별찍기-1
# 첫째 줄에 별 1개, 둘째 줄에 별 2개, n번째에 별 n개 찍는 프로그램
# 첫째 줄에 n 주워짐

t = int(input())
s = "*"
for i in range(t):
    print(s)
    s += "*"