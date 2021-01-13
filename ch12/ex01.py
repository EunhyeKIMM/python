import time 

t = time.time()
print(t)
print(time.ctime(t))

t = time.localtime(t)

print(f'{t.tm_year}:{t.tm_mon}:{t.tm_mday}')
print(f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}')