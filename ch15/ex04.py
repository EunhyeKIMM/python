def test1():
    print('test1 함수입니다. ')
def test2():
    print('test2 함수입니다. ')    


func = test1    # 참조를 전달 
func()

func = test2    # 참조를 전달 
func()

def test3(func):
    func()

test3(test1)    # func = test1
test3(test2)    # func = test2

