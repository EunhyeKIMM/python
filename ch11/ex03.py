info = """고길동 홍길동 둘리 도우너
30 40 50 60 
70 90 60 56 78 
80 100 20 90 100 
30 40 50 60"""

#{
#    '고길동': [30 40 50 60]
#        :
#    '도우너': [30 40 50 60]
#}

dic_info = zip(info.splitlines()[0].split(), info.splitlines()[1:])
print(dict(dic_info))

# map을 이용한 구현
#scores = [ list(map(int, line.split()))
#            for line in scores ]    # value
#print(scores)
#print()

# 한줄 코딩 보단 변수 분리 하는 코딩을 해보자 
# 숫자로 변경 작업도 !