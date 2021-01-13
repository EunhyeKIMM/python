def total(s, b):
    return s+b

score = [45, 89, 72, 53, 94]
bonus = [2, 3, 0, 0, 5]
for s in map(total, score, bonus):
    print(s, end = ", ")



# 문자열 정수로 바꾸기 
score = ['45', '89', '72', '53', '94']

for i, s in enumerate(score):
    score[i]= int(s)

print(score)
print(score[1]+score[2])

# 다른 방식 고안해보기 
score = ['45', '89', '72', '53', '94']

for i, n in (score, range(1, 5)):   # too much valuy error 
    score[n]= int(i)

print(score)


# map을 이용해 구하기 

score = ['45', '89', '72', '53', '94']
score = list(map(int, score))
print(score)

# functional programming (함수적 프로그래밍)
# filter, map, sort