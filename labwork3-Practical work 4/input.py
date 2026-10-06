import curses

def input_students(screen):
    screen.clear()
    screen.addstr(0, 0, "=== 1. INPUT STUDENTS ===")
    screen.addstr(1, 0, "Number of student(s): ")
    curses.echo()
    n = int(screen.getstr().decode('utf-8'))

    students_data = []
    for i in range(n):
        screen.addstr(3 + i * 4, 0, f"Student No:{i+1}")
        screen.addstr(4 + i * 4, 0, "Student ID: ")
        sid = screen.getstr().decode('utf-8')
        screen.addstr(5 + i * 4, 0, "Student name: ")
        name = screen.getstr().decode('utf-8')
        screen.addstr(6 + i * 4, 0, "Date of birth: ")
        dob = screen.getstr().decode('utf-8')
        students_data.append((sid, name, dob))

    curses.noecho()
    return students_data


def input_courses(screen):
    screen.clear()
    screen.addstr(0, 0, "=== 2. INPUT COURSES ===")
    screen.addstr(1, 0, "Number of course(s): ")
    curses.echo()
    n = int(screen.getstr().decode('utf-8'))

    courses_data = []
    for i in range(n):
        screen.addstr(3 + i * 5, 0, f"Course No:{i+1}")
        screen.addstr(4 + i * 5, 0, "Course ID: ")
        cid = screen.getstr().decode('utf-8')
        screen.addstr(5 + i * 5, 0, "Course name: ")
        cname = screen.getstr().decode('utf-8')
        screen.addstr(6 + i * 5, 0, "Course credit(s): ")
        credit = int(screen.getstr().decode('utf-8'))
        courses_data.append((cid, cname, credit))

    curses.noecho()
    return courses_data


def input_marks_for_course(screen, courses, students):
    screen.clear()
    if not courses:
        screen.addstr(0, 0, "No courses exist! Press any key...")
        screen.getch()
        return None, []

    screen.addstr(0, 0, "\n--- Course(s) List ---")
    row = 2
    for cid, course in courses.items():
        screen.addstr(row, 0, f"ID: {course.id} | Name: {course.name}")
        row += 1

    screen.addstr(row + 1, 0, "Course ID want to input mark: ")
    curses.echo()
    cid = screen.getstr().decode('utf-8')

    if cid not in courses:
        screen.addstr(row + 3, 0, "Course ID not found! Press any key...")
        curses.noecho()
        screen.getch()
        return None, []

    marks_data = []
    for idx, student in enumerate(students):
        screen.addstr(row + 3 + idx, 0, f"Mark of {student.name} (ID: {student.id}): ")
        raw_mark = float(screen.getstr().decode('utf-8'))
        marks_data.append((student.id, raw_mark))

    curses.noecho()
    return cid, marks_data