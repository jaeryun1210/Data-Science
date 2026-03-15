# a+b-4
# 두 정수 a,b 입력받고 a+b 출력하는 프로그램
'''
import sys
while True:
    try:
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break
        '''

import sys

for line in sys.stdin:
    a,b = map(int, line.split())
    print(a+b)

'''
EOF = end of file(더 이상 읽을 입력이 없다)
EX. 입력이 몇 줄 들어올지 모를 때 EOF까지 계속 처리
try-except로 예외처리 하거나 for문+sys.stdin로 처리
윈도우는 crtl+z, 맥,리눅스는 ctrl+d로 직접 입력가능
'''