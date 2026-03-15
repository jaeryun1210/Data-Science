# 서울의 오늘 날짜 출력하는 프로그램
from datetime import date

print(date.today())

#연-월-일 각각 쓸 때
'''today = date.today()
print(today.year, today.month, today.day)
'''
#형식 바꿔서 출력할 때
'''
today = date.today()
print(today.strftime("%y-%m-%d))
'''
#날짜+시간
'''
print(datetime.now())
'''