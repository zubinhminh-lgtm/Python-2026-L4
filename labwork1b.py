students = []
num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    s_id = input("  Student ID: ")
    name = input("  Student Name: ")
    dob = input("  DoB: ")
    students.append((s_id, name, dob))
courses = []
num_courses = int(input("\nEnter number of courses: "))
for _ in range(num_courses):
    c_id = input("  Course ID: ")
    c_name = input("  Course Name: ")
    courses.append((c_id, c_name))
print("\n--- LIST OF COURSES ---")
for c_id, c_name in courses:
    print(f"[{c_id}] {c_name}")
print("\n--- LIST OF STUDENTS ---")
for s_id, name, dob in students:
    print(f"[{s_id}] {name} - DoB: {dob}")
marks = {}
selected_course = input("\nSelect Course ID to enter marks: ")
print(f"Entering marks for course {selected_course}:")
for s_id, name, _ in students:
    mark = float(input(f"  Mark for {name} ({s_id}): "))
    marks[(selected_course, s_id)] = mark
print(f"\n--- MARKS FOR COURSE {selected_course} ---")
for s_id, name, _ in students:
    m = marks.get((selected_course, s_id), "N/A")
    print(f"Student: {name} ({s_id}) | Mark: {m}")