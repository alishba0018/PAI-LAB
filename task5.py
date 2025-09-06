def add_student(students, name, marks):
    students[name] = marks
    print(f"Added {name} with marks {marks}")
def update_marks(students, name, marks):
    if name in students:
        students[name] = marks
        print(f"Updated {name}'s marks to {marks}")
    else:
        print(f"{name} not found!")
def delete_student(students, name):
    if name in students:
        del students[name]
        print(f"Deleted {name}")
    else:
        print(f"{name} not found!")
def find_topper(students):
    if not students:
        print("No students available!")
        return
    topper = max(students, key=students.get) 
    print(f"Topper: {topper} with {students[topper]} marks")

students = {}
add_student(students, "Ali", 85)
add_student(students, "Sara", 92)
add_student(students, "Ahmed", 78)
update_marks(students, "Ali", 90)
delete_student(students, "Ahmed")
print("\nAll Students:", students)
find_topper(students)
