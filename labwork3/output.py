import curses
import numpy as np

def list_courses(screen, courses):
    screen.clear()
    if not courses:
        screen.addstr(0, 0, "No course exist! Press any key...")
        screen.getch()
        return

    screen.addstr(0, 0, "\n--- Course(s) List ---")
    row = 2
    for cid, course in courses.items():
        screen.addstr(row, 0, f"ID: {course.id} | Name: {course.name} | Credits: {course.credit}")
        row += 1

    screen.addstr(row + 1, 0, "\nPress any key to return...")
    screen.getch()


def list_students(screen, students, courses):
    screen.clear()
    if not students:
        screen.addstr(0, 0, "No student exist! Press any key...")
        screen.getch()
        return

    # Tính GPA và sắp xếp giảm dần bằng numpy
    for student in students:
        student.calculate_gpa(courses)

    gpas = np.array([s.gpa for s in students])
    sorted_indices = np.argsort(-gpas)
    sorted_students = [students[i] for i in sorted_indices]

    screen.addstr(0, 0, "\n--- Student(s) List (Sorted by GPA Descending) ---")
    screen.addstr(1, 0, f"{'ID':<12} | {'Name':<20} | {'DOB':<12} | {'GPA':<5}")
    screen.addstr(2, 0, "-" * 55)

    for idx, s in enumerate(sorted_students):
        screen.addstr(3 + idx, 0, f"{s.id:<12} | {s.name:<20} | {s.dob:<12} | {s.gpa:<5.2f}")

    screen.addstr(5 + len(sorted_students), 0, "\nPress any key to return...")
    screen.getch()


def all_course_marks(screen, courses, students):
    screen.clear()
    if not courses:
        screen.addstr(0, 0, "No courses exist! Press any key...")
        screen.getch()
        return

    screen.addstr(0, 0, "\n--- Course(s) List ---")
    row = 2
    for cid, course in courses.items():
        screen.addstr(row, 0, f"ID: {course.id} | Name: {course.name}")
        row += 1

    screen.addstr(row + 1, 0, "Check Course ID: ")
    curses.echo()
    cid = screen.getstr().decode('utf-8')
    curses.noecho()

    if cid not in courses:
        screen.addstr(row + 3, 0, "Course ID not found! Press any key...")
        screen.getch()
        return

    screen.addstr(row + 3, 0, f"\n--- Mark of course: {courses[cid].name} ---")
    found_any = False
    row_offset = 0
    for student in students:
        if cid in student.marks:
            screen.addstr(
                row + 5 + row_offset,
                0,
                f"Student: {student.name} (ID: {student.id}) - Mark: {student.marks[cid]}"
            )
            row_offset += 1
            found_any = True

    if not found_any:
        screen.addstr(row + 5, 0, "No marks exist for this course")

    screen.addstr(row + 7 + row_offset, 0, "\nPress any key to return...")
    screen.getch()