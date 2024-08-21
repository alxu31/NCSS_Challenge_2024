import json
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    math: int = 0
    english: int = 0
    science: int = 0
    history: int = 0
    comment: str = ""

    def print_report(self):
        print(f"Name: {self.name}")
        print(f"Math: {self.math}")
        print(f"English: {self.english}")
        print(f"Science: {self.science}")
        print(f"History: {self.history}")
        print(f"Comment: {self.comment}")
        print("------------------------")

students = []

with open('resources/reports.json') as jsonfile:
# with open('reports.json') as jsonfile:
    info = json.load(jsonfile)
    for item in info['reports']:
        students.append(Student(**item))



for student in students:
    student.print_report()