# 가중치를 전달해서, 가중치의 곱의 합을 리턴하세요.
def intsum(weight, *ints):  # 가변인수는 항사 마지막에 배치해야함
    total = 0
    for num in ints: 
        if num < 0: return  # return None과 동일
        total += num*weight

    return total

print(intsum(1.1, 1, 2, 3))
print(intsum(1.5, 5, 7, 9, 11, 13))
print(intsum(0.8, 8, 9, 6, 2, 9, 7, 5, 8))

total = intsum(1, 8, 9, 6, 2, -9, 7, 5, 8)
if total:
    print('total =', total)
else: 
    print("잘못된 데이터를 포함하고 있습니다.")

