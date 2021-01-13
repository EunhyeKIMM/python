dic = {
    'boy': '소년', 
    'school': '학교', 
    'book': '책'
}
print(dic)
print(dic['boy'])
print(dic['book'])
# print(dic['girl'])

print(dic.get('girl', '사전에 없는 단어 잆니다.'))

for i in dic:
    print(i)