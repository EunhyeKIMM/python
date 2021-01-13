# for student in [1, 2, 3, 4, 5]:
#    print("학생들의 성적을 처리한다.")

total = 0
for num in range(1, 101):
    total += num

print("total =", total)

for x in range(1, 51):
    if (x % 10) == 0:
        print('+', end = '')
    else:
        print('-', end = '')
