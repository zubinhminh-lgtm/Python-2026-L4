import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, courses_dict):
        if not self.marks:
            self.gpa = 0.0
            return 0

        marks_list = []
        credits_list = []
#cid, credit?
        for cid, mark in self.marks.items():
            if cid in courses_dict:
                marks_list.append(mark)
                credits_list.append(courses_dict[cid].credit)

        if credits_list and sum(credits_list) > 0:
            self.gpa = float(np.average(np.array(marks_list), weights=np.array(credits_list)))
            self.gpa = round(self.gpa, 2)
        else:
            self.gpa = 0.0
        return self.gpa
    