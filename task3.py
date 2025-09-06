students = [
    ("Ali", 85),
    ("Sara", 92),
    ("Ahmed", 78),
    ("Maya", 95),
    ("Zara", 88)
]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Students sorted by marks (descending):")
for student in sorted_students:
    print(student)
print("Top 3 Students:")
for student in sorted_students[:3]:
    print(student[0], "with marks:", student[1])
