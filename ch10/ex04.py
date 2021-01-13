# 단어 단위로 숫자 세기 

song = """by the rivers of babylon , there we sat down
yeah we wept, when we remember zion
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()

for line in song.splitlines():
    for c in line.split(' '):
        c = c.lower()
        if c not in alphabet:
            alphabet[c] = 1
        else:
            alphabet[c] += 1
        
# print(alphabet)

key = list(alphabet.keys())
key.sort()
for c in key:
    num = alphabet[c]
    print(c, '=', num)