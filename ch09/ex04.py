score = [
    [88, 76, 92, 98], 
    [65, 70, 58, 82], 
    [82, 80, 78, 88]
]

total = 0
totalsub = 0

for student in score:
    subject_total = 0
    for subject in student:
        subject_total += subject

    subjects = len(student)
    print("총점 %d, 평균 %.2f" % (
        subject_total, subject_total/subjects))
    total += subject_total
    totalsub += subjects

print("전제평균 %.2f" % (total/totalsub))