dates = "월화수목금토일"
print(dates[::2])
print(dates[::-1])

s = "python programming"
print(len(s))
print(s.find('o'))
print(s.rfind('o'))  # 뒤에서 부터 찾지만 앞의 인덱스 순번을 따름
print(s.index('r'))
print(s.count('n'))

print('a' in s)
print('z' in s)
print('pro' in s)
print('x' not in s)

name = "홍길동"

if name.startswith("홍"):
    print("홍씨입니다.")

if name.startswith("김"):
    print("김씨입니다.")

file = "figure.jpg"
if file.endswith(".jpg"):
    print("JPG 그림 파일입니다.")

# url 정보 찾기

url = "https://www.naver.com/blog/travel/seoul.html"

px = url.find(':')
if px != -1:
    protocol = url[:px]
else: 
    protocol = '없음'

fx = url.rfind('/')
if fx != -1:
    fname = url[fx+1:]
else: 
    fname = '없음'

tx = url.rfind('.')
if tx != -1:
    ftype = url[tx+1:]
else: 
    ftype = '없음'

print("프로토콜:", protocol)
print("파일명:", fname)
print("파일종류:", ftype)

