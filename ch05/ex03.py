# 문제 

# 컴퓨터와 가위바위보를 해서 승자 판정
# 컴퓨터는 랜덤하게 결정
# 사용자는 input으로 값 입력 

# 1. 정보의 표현 방법 결정
# 가위: 1
# 바위: 2
# 보: 3

# 2. [1, 2, 3] 중에서 랜덤하게 숫자 하나 결정
import random   # 모듈 --- 함수의 그룹/파일
# random.py 파일을 ex03.py 안으로 가져오겠다는 의미

com = random.randrange(1, 4) # end는 미포함 [1..4)

SCISSORS = 1
ROCK = 2
PAPER = 3

# 3. 사용자의 값 결정
user = int(input('가위(1), 바위(2), 보(3): '))
print(com)
# 4. 승부 판정
if user == SCISSORS:
    if com == ROCK:
        print('패배')
    elif com == SCISSORS:
        print("비김")
    elif com == PAPER:
        print("승리")
elif user == ROCK:
    if com == PAPER:
        print('패배')
    elif com == ROCK:
        print("비김")
    elif com == SCISSORS:
        print("승리")
elif user == PAPER:
    if com == SCISSORS:
        print('패배')
    elif com == PAPER:
        print("비김")
    elif com == ROCK:
        print("승리")        



