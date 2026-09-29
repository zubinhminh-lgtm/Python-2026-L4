def input_students():
    n = int(input("Number of student(s): "))
    students = []
    for i in range(n):
        print(f"Student No:{i+1}")
        StuID = input("Student ID: ")
        Name = input("Student name: ")
        Dob = input("Date of birth: ")
        students.append({"ID": StuID, "Name": Name, "DOB": Dob})
    return students

def input_courses():
    n = int(input("Number of course(s): "))
    courses = []
    for i in range(n):
        print(f"Course No:{i+1}")
        CID = input("Course ID: ")
        Cname = input("Course name: ")
        courses.append({"ID": CID, "Name": Cname})
    return courses

def findCID(courses, course_id):
    for course in courses:
        if course["ID"] == course_id:
            return course
    return None

def list_courses(courses):
    if not courses:
        print("No course exist")
        return
    print("\n--- Course(s) List ---")
    for course in courses:
        print(f"ID: {course['ID']} | Name: {course['Name']}")

def list_students(students):
    if not students:
        print("No student exist")
        return
    print("\n--- Student(s) List ---")
    for student in students:
        print(f"ID: {student['ID']} | Name: {student['Name']} | DOB: {student['DOB']}")

def input_marks(students, courses, marks):
    if not courses:
        print("No courses exist")
        return

    list_courses(courses)
    course_id = input("Course ID want to input mark: ")
    course = findCID(courses, course_id)
    
    if course is None:
        print("Course ID not found")
        return
    
    if course_id not in marks:
        marks[course_id] = {}
        
    for student in students:
        mark = float(input(f"Mark of {student['Name']} (ID: {student['ID']}): "))
        marks[course_id][student["ID"]] = mark

def all_course_marks(students, courses, marks):
    if not courses:
        print("No courses exist")
        return
    
    list_courses(courses)
    CID = input("Check Course ID: ")
    course = findCID(courses, CID)
    
    if course is None:
        print("Course ID not found")
        return
    
    print(f"\n--- Mark of course: {course['Name']} ---")
    course_marks = marks.get(CID, {})
    
    if not course_marks:
        print("No marks exist for this course")
        return
    
    for student in students:
        mark = course_marks.get(student["ID"])
        if mark is not None:
            print(f"Student: {student['Name']} (ID: {student['ID']}) - Mark: {mark}")

def main():
    students = []
    courses = []
    marks = {}
    
    while True:
        print("\n   MENU ")
        print("1. Input student(s)")
        print("2. Input course(s)")
        print("3. Input mark(s)")
        print("4. Course(s) List")
        print("5. Student(s) List")
        print("6. Marks(s) List")
        print("0. Exit")
        
        choice = input("Action: ")
        
        if choice == "1":
            students = input_students()
        elif choice == "2":
            courses = input_courses()
        elif choice == "3":
            input_marks(students, courses, marks)
        elif choice == "4":
            list_courses(courses)
        elif choice == "5":
            list_students(students)
        elif choice == "6":
            all_course_marks(students, courses, marks)
        elif choice == "0":
            print("Exited")
            break
        else:
            print("Not valid, try again")

main()
