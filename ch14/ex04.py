def load(fpath):
    with open(fpath, "rt") as f:
        return f.readlines()

def main():
    try:
        lines = load('data.csv')
        print(lines)
    except Exception as e:
        print('예외 발생', e)

main()