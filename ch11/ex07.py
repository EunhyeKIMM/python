# 얕은 복사 

list0 = ['a', "b"]
list1 = [list0, 1, 2]
list2 = list1.copy()

list2[0][1] = 'c'   # 참조는 참조로 복사가 된다. 값은 값으로 복사 
print(list1)
print(list2)

# 깊은 복사 

import copy

list0 = ['a', "b"]
list1 = [list0, 1, 2]
list2 = copy.deepcopy(list1)

list2[0][1] = 'c'
print(list1)
print(list2)

# 전체 대입은 내용을 바꿀 수 없다
#def test(l):
#    l = [10, 20, 30]

#l = [1, 2, 3]
#test(l)
#print(l)   ==> 결과: [1, 2, 3]