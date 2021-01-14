def inner():
    print("결과를 출력합니다.")

def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-"*20)
    return wrapper 

# outer(inner)

# def hello():
#     print("안녕하세요")

# outer(hello)

inner = outer(inner)
inner()