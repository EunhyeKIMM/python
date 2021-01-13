def calcstep(**args):
    print(args)
    begin = args['begin']
    end = args['end']
    step = args['step']
    # step = args.get('step', 1) => 디폴트 값을 주는 효과 

    total = 0
    for num in range(begin, end +1, step):
        total += num

        return total 


# print("3 ~ 5 =", calcstep(begin=3, end=5))
print("3 ~ 5 =", calcstep(begin=3, end=5, step=1 ))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))