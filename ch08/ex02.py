s = "python"
for i in range(len(s)):
    print(s[i], end = ",")
print("\n")

file = "20200101-104831.jpg"
print("촬영 날짜" + file[4:6] + "월" + file[6:8] + "일")
print("촬영 시간" + file[9:11] + "월" + file[11:13] + "일")
print("확장자" + file[-3:])

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

print("생일: ", year, "-", month, "-", date, sep='')
print("지역코드:", socialnum[8:10])