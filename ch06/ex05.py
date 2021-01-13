score = [92, 86, 68, -1, 56]
error_num = 0
for s in score:
    if s == -1:
        error_num += 1 
        continue
    print(s)
print("에러의 갯수는 =", error_num)
print("성적 처리 끝")