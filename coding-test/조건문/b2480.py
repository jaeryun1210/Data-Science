# 주사위 세개
# 수학,구현,사칙연산,많은 조건 분기
'''
같은 눈 3개 : 10000+(같은 눈)*1000
같은 눈 2개 : 1000+(같은 눈)*100
다른 눈 : (가장 큰 눈)*100
의 상금을 계산하는 프로그램
'''
a,b,c = map(int, input().split())

if a==b==c:
    print(10000 + a * 1000)
elif (a==b and a!=c) | (b==c and a!=b) | (a==c and b!=c):
    if a==b or a==c:
        print(1000+a*100)
    else:
        print(1000+b*100)
else:
    print((max(a,b,c))*100)

'''
a,b,c = map(int, input().split())

if(a==b and b==c):
    print(10000+(a*1000))
elif(a==b) or (a==c):
    print(1000+(a*100))
elif(b==c):
    print(1000+(b*100))
else:
    print(max(a,b,c)*100)
'''