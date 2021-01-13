dates = ["월", "화", "수", "목", "금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]

menu = zip(dates, food)
# menu = list(zip(dates, food))  보통 이 형태로 zip사용
# zip의 특징을 알아봐 보자..@!

for d, f in menu:
    print("%s요일 메뉴: %s" % (d, f))

menu_dic = dict(zip(dates, food))
print(menu_dic)