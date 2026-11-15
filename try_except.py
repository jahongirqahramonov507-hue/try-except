# 1-masala
def count_passing_students(grades, passingGrade):
    count=0
    for ball in grades:
        try:
            if ball<0: 
                raise ValueError("ball musbat bo'lishi kerak!")
            elif ball>100:
                raise ValueError("ball<=100")
            elif ball >= passingGrade:
                count+=1
        except ValueError as xato:
            print(xato)


    return count


grades = [45, 60, 75, 30, -100,90]
passingGrade = 60
print(count_passing_students(grades, passingGrade))
# Output: 3
