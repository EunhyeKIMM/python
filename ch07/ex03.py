def calcstep(begin, end=1, step=1): # 뒤에서 부터 디폴트값 지정 가능
    total = 0
    for num in range(begin, end +1, step):
        total += num

    return total

print("1 ~ 10 =", calcstep(1, 10, 2))
print("1 ~ 100 =", calcstep(1, 100))