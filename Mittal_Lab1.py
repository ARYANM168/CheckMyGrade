import csv
import hashlib
import time
import statistics

STUDENT_FILE = "students.csv"
COURSE_FILE = "courses.csv"
PROFESSOR_FILE = "professors.csv"
LOGIN_FILE = "login.csv"

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def read_csv(file):
    data = []
    try:
        with open(file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data


def write_csv(file, fieldnames, data):
    with open(file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

class Student:

    def display_records(self):
        students = read_csv(STUDENT_FILE)
        for s in students:
            print(s)

    def add_new_student(self):
        email = input("Email: ")
        first = input("First Name: ")
        last = input("Last Name: ")
        course = input("Course ID: ")
        grade = input("Grade: ")
        marks = input("Marks: ")

        students = read_csv(STUDENT_FILE)

        students.append({
            "Email_address": email,
            "First_name": first,
            "Last_name": last,
            "Course_id": course,
            "Grade": grade,
            "Marks": marks
        })

        write_csv(STUDENT_FILE,
                  ["Email_address", "First_name", "Last_name", "Course_id", "Grade", "Marks"],
                  students)

    def delete_student(self):
        email = input("Enter email to delete: ")
        students = read_csv(STUDENT_FILE)
        students = [s for s in students if s["Email_address"] != email]

        write_csv(STUDENT_FILE,
                  ["Email_address", "First_name", "Last_name", "Course_id", "Grade", "Marks"],
                  students)

    def update_student_record(self):
        email = input("Enter email to update: ")
        students = read_csv(STUDENT_FILE)

        for s in students:
            if s["Email_address"] == email:
                s["Marks"] = input("New marks: ")
                s["Grade"] = input("New grade: ")

        write_csv(STUDENT_FILE,
                  ["Email_address", "First_name", "Last_name", "Course_id", "Grade", "Marks"],
                  students)

    def search_student(self):
        email = input("Enter email to search: ")
        students = read_csv(STUDENT_FILE)

        start = time.time()

        for s in students:
            if s["Email_address"] == email:
                print(s)

        end = time.time()
        print("Search time:", end - start)

    def statistics(self):
        students = read_csv(STUDENT_FILE)
        marks = [int(s["Marks"]) for s in students if s["Marks"].isdigit()]

        if marks:
            print("Average:", sum(marks)/len(marks))
            print("Median:", statistics.median(marks))

class Course:

    def display_courses(self):
        courses = read_csv(COURSE_FILE)
        for c in courses:
            print(c)

    def add_new_course(self):
        cid = input("Course ID: ")
        name = input("Course Name: ")
        desc = input("Description: ")

        courses = read_csv(COURSE_FILE)

        courses.append({
            "Course_id": cid,
            "Course_name": name,
            "Description": desc
        })

        write_csv(COURSE_FILE,
                  ["Course_id", "Course_name", "Description"],
                  courses)

class Professor:

    def display_professors(self):
        profs = read_csv(PROFESSOR_FILE)
        for p in profs:
            print(p)

    def add_new_professor(self):
        email = input("Professor Email: ")
        name = input("Name: ")
        rank = input("Rank: ")
        course = input("Course ID: ")

        profs = read_csv(PROFESSOR_FILE)

        profs.append({
            "Professor_id": email,
            "Professor_Name": name,
            "Rank": rank,
            "Course_id": course
        })

        write_csv(PROFESSOR_FILE,
                  ["Professor_id", "Professor_Name", "Rank", "Course_id"],
                  profs)

class LoginUser:

    def register(self):
        email = input("Email: ")
        password = input("Password: ")
        role = input("Role (student/professor): ")

        encrypted = encrypt_password(password)

        users = read_csv(LOGIN_FILE)

        users.append({
            "User_id": email,
            "Password": encrypted,
            "Role": role
        })

        write_csv(LOGIN_FILE, ["User_id", "Password", "Role"], users)

    def login(self):
        email = input("Email: ")
        password = input("Password: ")

        encrypted = encrypt_password(password)

        users = read_csv(LOGIN_FILE)

        for u in users:
            if u["User_id"] == email and u["Password"] == encrypted:
                print("Login successful")
                return True

        print("Login failed")
        return False

def main_menu():

    student = Student()
    course = Course()
    professor = Professor()

    while True:
        print("\nCheckMyGrade Menu")
        print("1. Show Students")
        print("2. Add Student")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Student Statistics")
        print("7. Show Courses")
        print("8. Add Course")
        print("9. Show Professors")
        print("10. Add Professor")
        print("11. Exit")

        input = input("Enter your number: ")

        if input == "1":
            student.display_records()

        elif input == "2":
            student.add_new_student()

        elif input == "3":
            student.delete_student()

        elif input == "4":
            student.update_student_record()

        elif input == "5":
            student.search_student()

        elif input == "6":
            student.statistics()

        elif input == "7":
            course.display_courses()

        elif input == "8":
            course.add_new_course()

        elif input == "9":
            professor.display_professors()

        elif input == "10":
            professor.add_new_professor()

        elif input == "11":
            break

        else:
            print("Invalid option")

login = LoginUser()

print("1. Register")
print("2. Login")

c = input("Enter your number: ")

if c == "1":
    login.register()

if login.login():
    main_menu()
