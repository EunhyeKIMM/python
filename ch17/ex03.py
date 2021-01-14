def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2]

solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
# 함수를 실행 시키라는 것이 아닌 제너레이터로 바꿔라 라는 뜻..? 
# 함수 실행이 아닌 제너레이터 객체로 변환 작업이 이루어짐
print(solarterm)
print(dir(solarterm))

for k in solarterm:
    print(k, end=',')