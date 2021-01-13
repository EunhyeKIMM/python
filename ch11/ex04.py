adult = [True, False, True, False]

print(any(adult))
print(all(adult))

def flunk(s):
    return s < 60

score = [45, 89, 72, 53, 94]
for s in filter(lambda s: s<60, score):
    print(s)

score2 = [ n for n in score if n <60]   # 파이썬 유일 기능
print(score2)
score2 = list(filter(lambda a: a<60, score))
print(score2)