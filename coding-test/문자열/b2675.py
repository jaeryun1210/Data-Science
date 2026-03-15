# 문자열 반복
# 문자 s를 입력받은 후, 각 문자를 r번 반복해 
# 새 문자열 p를 만든 후 출력하는 프로그램

t = int(input())

for _ in range(t):
    r,s = input().split()
    r = int(r)

    p = ""
    for c in s:
        p += c * r
    print(p)
    # print(''.join(c*r for c in s))

'''
map(함수,데이터) 개념
어떤 데이터에 같은 함수를 적용하는 것
'''