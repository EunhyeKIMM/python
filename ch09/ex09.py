ans = input("결제 하시겠습니까? ")

# ans.lower()
# print(ans) 실행 실패...

if ans in ['yes', 'y', 'ok', '예']:
    print("결제를 진행합니다.")
else:
    print("결제를 취소합니다.")
