marks = {'Alice': 91, 'Bob': 76, 'Charlie': 85, 'David': 95}

grades = {name: ('A' if mark >= 90 else 'B' if mark >= 80 else 'C' ) for name, mark in marks.items()}
print("Grades Dictionary:", grades)

