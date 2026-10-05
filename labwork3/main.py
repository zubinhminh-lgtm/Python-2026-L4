import curses
from domains import Student, Course, Mark
import input as input_mod
import output as output_mod

def main(screen):
    students = []
    courses = {}

    while True:
        screen.clear()
        screen.addstr(0, 0, "   MENU ")
        screen.addstr(1, 0, "1. Input student(s)")
        screen.addstr(2, 0, "2. Input course(s)")
        screen.addstr(3, 0, "3. Input mark(s)")
        screen.addstr(4, 0, "4. Course(s) List")
        screen.addstr(5, 0, "5. Student(s) List")
        screen.addstr(6, 0, "6. Marks(s) List")
        screen.addstr(7, 0, "0. Exit")
        screen.addstr(9, 0, "Action: ")

        curses.echo()
        choice = screen.getstr().decode('utf-8')
        curses.noecho()

        if choice == "1":
            s_data = input_mod.input_students(screen)
            for sid, name, dob in s_data:
                students.append(Student(sid, name, dob))
        elif choice == "2":
            c_data = input_mod.input_courses(screen)
            for cid, cname, credit in c_data:
                courses[cid] = Course(cid, cname, credit)
        elif choice == "3":
            cid, marks_data = input_mod.input_marks_for_course(screen, courses, students)
            if cid:
                for sid, raw_score in marks_data:
                    mark_obj = Mark(sid, cid, raw_score)
                    for s in students:
                        if s.id == sid:
                            s.marks[cid] = mark_obj.score
        elif choice == "4":
            output_mod.list_courses(screen, courses)
        elif choice == "5":
            output_mod.list_students(screen, students, courses)
        elif choice == "6":
            output_mod.all_course_marks(screen, courses, students)
        elif choice == "0":
            break


if __name__ == "__main__":
    curses.wrapper(main)