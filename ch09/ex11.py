score = [88, 95, 70, 100, 99]
sorted_score = sorted(score)

print(score)
print(sorted_score)
print()

score = (88, 95, 70, 100, 99)
total = 0

for s in score:
    total += s

print("총점: ", total)
print("평균: ", total/len(score))
print(score)