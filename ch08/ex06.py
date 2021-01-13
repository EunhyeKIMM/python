trabler ="""
강나루 건너서
밀밭 길을 

구름에 달 가듯이 
가는 나그네
"""

poet = trabler.splitlines()
for line in poet:
    print(line)


s = "독도는 일본땅. 대마도도 일본땅"
print(s)
print(s.replace("일본", "한국"))

message = "안녕하세요"
print(message.center(30))
print(message.ljust(30))
print(message.rjust(30))