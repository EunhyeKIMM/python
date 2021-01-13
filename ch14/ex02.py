
try:
    # f = open("live.txt", "rt")
    with open("live.txt", "rt") as f:
        text = f.read() # 예외 발생시 with 블럭을 벗어날때 close() 자동호출됨
        print(text)
except Exception as e:
    print('예외발생', e)



#     print("파일이 없습니다.")
# finally:
#     if f:
#         f.close()