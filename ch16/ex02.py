import ex01
import m1

print('ex02.py', __name__)
print(m1.calcsum(20))

if __name__ == '__main__':
    print(dir(m1))
    print(m1.__file__)
    

# 모듈은 내부적으로 캐시가 관리하고 있다. 