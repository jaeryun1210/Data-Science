# 알파벳 찾기

s = input()

for a in 'abcdefghijklmnopqrstuvwxyz':
    print(s.find(a), end=' ')

'''
문자열.find(찾을문자)
문자가 있으면 : 처음 등장하는 위치
문자가 없으면 -1 반환
index()는 문자가 없을 경우 에러발생
'''