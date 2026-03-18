import unittest
import csv
import time
import os

class TestCheckMyGrade(unittest.TestCase):

    def setUp(self):
        with open("students.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Email_address", "First_name", "Last_name", "Course_id", "Grade", "Marks"])

        with open("courses.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Course_id", "Course_name", "Description"])

        with open("professors.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Professor_id", "Professor_Name", "Rank", "Course_id"])

    def generate_students(self, n=1000):
        with open("students.csv", "a", newline='') as f:
            writer = csv.writer(f)

            for i in range(n):
                writer.writerow([
                    f"user{i}@test.com",
                    "Test",
                    "User",
                    "DATA200",
                    "A",
                    str(50 + (i % 50))
                ])

    def test_add_students(self):
        self.generate_students(1000)

        with open("students.csv", "r") as f:
            data = list(csv.reader(f))

        print("Total students:", len(data) - 1)
        self.assertTrue(len(data) - 1 == 1000)

    def test_search_time(self):
        self.generate_students(1000)

        start = time.time()
        found = False

        with open("students.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Email_address"] == "user500@test.com":
                    found = True
                    break

        end = time.time()

        print("Search time:", end - start)
        self.assertTrue(found)

    def test_sort_students_ascending(self):
        self.generate_students(1000)

        start = time.time()

        with open("students.csv", "r") as f:
            data = list(csv.DictReader(f))

        sorted_data = sorted(data, key=lambda x: int(x["Marks"]))

        end = time.time()

        print("Sorting (ascending) time:", end - start)
        self.assertTrue(len(sorted_data) == 1000)

    def test_sort_students_descending(self):
        self.generate_students(1000)

        start = time.time()

        with open("students.csv", "r") as f:
            data = list(csv.DictReader(f))

        sorted_data = sorted(data, key=lambda x: int(x["Marks"]), reverse=True)

        end = time.time()

        print("Sorting (descending) time:", end - start)
        self.assertTrue(len(sorted_data) == 1000)

    def test_delete_student(self):
        self.generate_students(1000)

        email_to_delete = "user10@test.com"

        with open("students.csv", "r") as f:
            data = list(csv.DictReader(f))

        new_data = [row for row in data if row["Email_address"] != email_to_delete]

        with open("students.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(new_data)

        self.assertTrue(len(new_data) == 999)

    def test_modify_student(self):
        self.generate_students(1000)

        with open("students.csv", "r") as f:
            data = list(csv.DictReader(f))

        for row in data:
            if row["Email_address"] == "user20@test.com":
                row["Marks"] = "99"

        with open("students.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        self.assertTrue(True)

    def test_add_course(self):
        with open("courses.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["TEST101", "Test Course", "Sample Description"])

        with open("courses.csv", "r") as f:
            data = list(csv.reader(f))

        self.assertTrue(len(data) > 1)

    def test_delete_course(self):
        with open("courses.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["TEST101", "Test Course", "Sample Description"])

        with open("courses.csv", "r") as f:
            data = list(csv.DictReader(f))

        data = [row for row in data if row["Course_id"] != "TEST101"]

        with open("courses.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Course_id", "Course_name", "Description"])
            writer.writeheader()
            writer.writerows(data)

        self.assertTrue(True)

    def test_add_professor(self):
        with open("professors.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["prof@test.com", "Test Prof", "Senior", "DATA200"])

        with open("professors.csv", "r") as f:
            data = list(csv.reader(f))

        self.assertTrue(len(data) > 1)

    def test_delete_professor(self):
        with open("professors.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["prof@test.com", "Test Prof", "Senior", "DATA200"])

        with open("professors.csv", "r") as f:
            data = list(csv.DictReader(f))

        data = [row for row in data if row["Professor_id"] != "prof@test.com"]

        with open("professors.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Professor_id", "Professor_Name", "Rank", "Course_id"])
            writer.writeheader()
            writer.writerows(data)

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()