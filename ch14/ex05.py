def load(fpath):
    with open(fpath, "rt") as f:    # encoding="utf-8"
        return f.readlines()

def convert(lines):   #학생이름 key, 성적리스트: value --> 사전을 리턴
    data = {}
    for line in lines[1:]:  # 헤더는 제외
        items = line.split(',')
        name = items[0]     # 이름
        scores = items[1:]  # 성적 리스트
        data[name] = list(map(int, scores)) #사전에 추가, white 문자(공백, 탭, 엔터)

    return data

def main():
    try:
        # lines = load('data.csv')
        fpath = input('파일명: ')
        lines = load(fpath)
        print(lines)
        data = convert(lines)
        print(data)

    except Exception as e:
        print('예외 발생', e)

main()

# 눈물... csv파일 꺠지는거 해결하고 해보깅...ㅜㅜ...