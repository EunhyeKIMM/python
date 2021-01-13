stack = []

# 스택으로 데이터를 저장해야 됩니다. 
stack.append(10)    # [10]
stack.append(20)    # [10, 20]
stack.append(30)    # [10, 20, 30]

# 스택에 있는 데이터를 출력합니다.
v1 = stack.pop()    # v1 = 30/ [10, 20]
v2 = stack.pop()    # v2 = 20/ [10]
v3 = stack.pop()    # v3 = 10/ []

# Queue는 .pop(0)을 사용 