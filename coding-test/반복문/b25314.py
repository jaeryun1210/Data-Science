# 코딩은 체육과목입니다
# 4바이트당 long 하나를 저장할 수 있다고 생각되는 정수 자료형의 이름을 출력하는 프로그램
# 구현

n = int(input())

n = (n//4)-1
st = "long "

for i in range(n):
    st = st +"long "

print(f"{st}int")
'''
x = int(input())
n = x // 4
for i in range(n):
    print("long", end = " ")
print("int")
'''