# '생년-월-일'로 포맷팅해서 출력
# 출신 지역 코드 출력

socialnum = '001212-3451231'

year = socialnum[:2]
month = socialnum[2:4]
date = socialnum[4:6]
region = socialnum[8:10]
ger = socialnum[7]

if ger == '1' or ger == '2':
    year = '19' + year
else: 
    year = '20' + year

age = 20

print("생일: ", year, "-", month, "-", date, sep='')
print("지역코드:", socialnum[8:10])

print("f-string기법으로 출력하기")
print(f"생일: {year}-{month}-{date}, age: {age}")
print(f"지역코드: {region}")