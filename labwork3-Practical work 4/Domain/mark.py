import math

class Mark:
    def __init__(self, student_id, course_id, raw_score):
        self.student_id = student_id
        self.course_id = course_id
        # Làm tròn xuống 1 chữ số thập phân dùng math.floor()
        self.score = math.floor(raw_score * 10) / 10.0