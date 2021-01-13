# ch07의 20p

def calcscore(name, *score, **option):  # 실전에서 많이 나옴 
    print(name)
    total = 0
    for s in score:
        total += s

    print("총점: ", total)
    if(option.get(avg, False) == True):
        print("평균: ", total/len(score))

calcscore("홍길동", 88, 99, 77, avg=True)
calcscore("고길동", 99, 88, 95, 85, avg=False)
calcscore("둘리", 99, 85, 20, 40, 80)

#def some(*args, **kargs):
#    pass

#some()
#some(1)
#error 수정해야함