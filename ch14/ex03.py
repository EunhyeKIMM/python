try:
    with open("live.txt", "rt", endcoding="utf-8") as f:
        rows = f.readlines()
        for ix, row in enumerate(rows, 1):
            print(f'{ix}: {row}', end='')

except Exception as e:
    print('예외발생', e)