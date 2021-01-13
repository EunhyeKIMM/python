price = 1000

def sale():
    global price
    price = 500 # 함수 안에서는 지역 변수

sale()
print(price)