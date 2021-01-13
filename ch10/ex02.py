dic = {
    'boy': '소년', 
    'school': '학교', 
    'book': '책'
}

dic['boy'] = '남자아이' # 기존 boy를 덮어써버림
dic['girl'] = '소녀'
del dic['book'] 
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

for key, value in dic.items():
    print(key, value)

dic2 = {
    'student': '학생', 'teacher': '선생님', 'book': '서적'
}

dic.update(dic2)    # key값이 겹치는 건 dic2의 값으로 덮어씌워버림
print(dic)