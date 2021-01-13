score = [45, 89, 72, 53, 94]
for s in map(lambda x: x/2, score):
    print(s, end = ', ')


# 60점 이하인 성적이 포함되있는지 판단하세요.
# 과락 여부 판단 
# map, any 함수 

score = [45, 89, 72, 53, 94]

result = list(map(lambda x: x<60, score))
print(any(result))

