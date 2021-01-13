str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError:
    print("점수의 형식이 잘못되었습니다.")
except IndexError:
    print("첨자의 범위를 벗어났습니다. ")

print("작업완료")    

str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]
except (ValueError, IndexError):
    print("점수의 형식이나 첨자가 잘못되었습니다.")

print("작업완료")  

str = "89점"
try:
    score = int(str)
    print(score)
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)

print("작업완료")  