import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, courses):
        if not self.marks:
            self.gpa = 0.0
            return 0.0
        
        marks_list = []
        credits_list = []
        
        for course_id, mark in self.marks.items():
            if course_id in courses:
                marks_list.append(mark)
                credits_list.append(courses[course_id].credit)
        
        if credits_list and sum(credits_list) > 0:
            self.gpa = float(np.average(np.array(marks_list), weights=np.array(credits_list)))
            self.gpa = round(self.gpa, 2)
        else:
            self.gpa = 0.0
        return self.gpa

class Course:
    def __init__(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        self.credit = credit

class SchoolManagement:
    def __init__(self):
        self.students = []
        self.courses = {}

    def input_students(self, screen):
        screen.clear()
        screen.addstr(0, 0, "INPUT STUDENTS")
        screen.addstr(1, 0, "Number of students: ")
        curses.echo()
        n = int(screen.getstr().decode('utf-8'))
        
        for i in range(n):
            screen.addstr(3 + i * 4, 0, f"Student {i+1}")
            screen.addstr(4 + i * 4, 0, "ID: ")
            sid = screen.getstr().decode('utf-8')
            screen.addstr(5 + i * 4, 0, "Name: ")
            name = screen.getstr().decode('utf-8')
            screen.addstr(6 + i * 4, 0, "DOB: ")
            dob = screen.getstr().decode('utf-8')
            self.students.append(Student(sid, name, dob))
        curses.noecho()

    def input_courses(self, screen):
        screen.clear()
        screen.addstr(0, 0, "INPUT COURSES")
        screen.addstr(1, 0, "Number of courses: ")
        curses.echo()
        n = int(screen.getstr().decode('utf-8'))
        
        for i in range(n):
            screen.addstr(3 + i * 4, 0, f"Course {i+1}")
            screen.addstr(4 + i * 4, 0, "ID: ")
            cid = screen.getstr().decode('utf-8')
            screen.addstr(5 + i * 4, 0, "Name: ")
            cname = screen.getstr().decode('utf-8')
            screen.addstr(6 + i * 4, 0, "Credits: ")
            credit = int(screen.getstr().decode('utf-8'))
            self.courses[cid] = Course(cid, cname, credit)
        curses.noecho()

    def input_marks(self, screen):
        screen.clear()
        if not self.courses:
            screen.addstr(0, 0, "No courses available! Press any key...")
            screen.getch()
            return

        screen.addstr(0, 0, "INPUT MARKS")
        screen.addstr(1, 0, "Select Course ID: ")
        curses.echo()
        cid = screen.getstr().decode('utf-8')
        
        if cid not in self.courses:
            screen.addstr(3, 0, "Course not found! Press any key...")
            curses.noecho()
            screen.getch()
            return

        for idx, student in enumerate(self.students):
            screen.addstr(3 + idx, 0, f"Mark for {student.name} (ID: {student.id}): ")
            raw_mark = float(screen.getstr().decode('utf-8'))
            
            # Làm tròn xuống 1 chữ số thập phân dùng math.floor()
            # Ví dụ: 8.57 -> 85.7 -> floor(85.7) = 85 -> 8.5
            rounded_mark = math.floor(raw_mark * 10) / 10.0
            student.marks[cid] = rounded_mark
            
        curses.noecho()

    def sort_students_by_gpa(self):
        for student in self.students:
            student.calculate_gpa(self.courses)
        gpas = np.array([s.gpa for s in self.students])
        sorted_indices = np.argsort(-gpas)  # Dấu trừ để sắp xếp giảm dần
        self.students = [self.students[i] for i in sorted_indices]

    def display_students(self, screen):
        screen.clear()
        self.sort_students_by_gpa()
        
        screen.addstr(0, 0, "STUDENT LIST (SORTED BY GPA DESCENDING)")
        screen.addstr(1, 0, f"{'ID':<10} | {'Name':<20} | {'DOB':<12} | {'GPA':<5}")
        screen.addstr(2, 0, "-" * 55)
        
        for idx, s in enumerate(self.students):
            screen.addstr(3 + idx, 0, f"{s.id:<10} | {s.name:<20} | {s.dob:<12} | {s.gpa:<5.2f}")
            
        screen.addstr(5 + len(self.students), 0, "Press any key to return...")
        screen.getch()

def main(screen):
    app = SchoolManagement()
    
    while True:
        screen.clear()
        screen.addstr(0, 0, "SCHOOL MANAGEMENT (CURSES UI)")
        screen.addstr(1, 0, "1. Input Student(s)")
        screen.addstr(2, 0, "2. Input Course(s)")
        screen.addstr(3, 0, "3. Input Mark(s)")
        screen.addstr(4, 0, "4. List Students & GPA")
        screen.addstr(5, 0, "0. Exit")
        screen.addstr(7, 0, "Choose an option: ")
        
        curses.echo()
        choice = screen.getstr().decode('utf-8')
        curses.noecho()
        
        if choice == "1":
            app.input_students(screen)
        elif choice == "2":
            app.input_courses(screen)
        elif choice == "3":
            app.input_marks(screen)
        elif choice == "4":
            app.display_students(screen)
        elif choice == "0":
            break

if __name__ == "__main__":
    curses.wrapper(main)