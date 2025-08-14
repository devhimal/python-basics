student_db = []

def add_student(name, age, grade):
    student_db.append({"name": name, "age": age, "grade": grade})

def query_student(name):
    for student in student_db:
        if student["name"] == name:
            return student
    return "Student not found"

# Create a few students
add_student("Alice", 20, "A")
add_student("Bob", 21, "B")
print("Student Database:", student_db)
print("Querying Alice:", query_student("Alice"))
