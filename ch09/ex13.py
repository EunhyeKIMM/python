import time 

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("지금은 %d시 %d분 입니다. " %(result[0], result[1]))

hour, minute = gettime()
print("지금은 %d시 %d분 입니다. " %(hour, minute))