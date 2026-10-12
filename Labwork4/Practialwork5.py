import os
import zipfile

DATA_FILE = "students.dat"
TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]

def write_students(students):
    """Writes student info to students.txt[cite: 1]"""
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['id']},{s['name']},{s['dob']}\n")

def write_courses(courses):
    """Writes course info to courses.txt[cite: 1]"""
    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c['id']},{c['name']},{c['credits']}\n")

def write_marks(marks):
    """Writes marks to marks.txt[cite: 1]"""
    with open("marks.txt", "w") as f:
        for m in marks:
            f.write(f"{m['course_id']},{m['student_id']},{m['mark']}\n")

def compress_files():
    """Compresses text files into students.dat[cite: 2]"""
    with zipfile.ZipFile(DATA_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in TXT_FILES:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)  # Clean up uncompressed files optional

def load_data():
    """Decompresses students.dat and loads data upon startup[cite: 2]"""
    students, courses, marks = [], [], []

    if not os.path.exists(DATA_FILE):
        print("No existing archive found. Starting fresh.")
        return students, courses, marks

    with zipfile.ZipFile(DATA_FILE, "r") as zipf:
        zipf.extractall()

    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append({"id": parts[0], "name": parts[1], "dob": parts[2]})

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append({"id": parts[0], "name": parts[1], "credits": parts[2]})

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    marks.append({"course_id": parts[0], "student_id": parts[1], "mark": parts[2]})

    print("Data successfully decompressed and loaded.")
    return students, courses, marks

def main():
    students, courses, marks = load_data()

    compress_files()
    print("Archive updated and saved to students.dat. Good bye!")

if __name__ == "__main__":
    main()