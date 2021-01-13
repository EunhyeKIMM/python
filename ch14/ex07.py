import pickle 
import sys
# python ex07.py data.dat
# sys.argv

# def load(fpath):
#     with open(fpath, 'wb') as f:
#         return pickle.load(f)

def load(fpath):
    with open(fpath, 'rb') as f:
        return pickle.load(f)        

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print('파일명을 입력하세요')
        print('예) python ex07.py filename')
        sys.exit(0)

    fname = sys.argv[1]

    try:
        # data =load('data.dat')
        data = load(fname)
        print(data)
    except Exception as e:
        print('예외발생', e)

main()