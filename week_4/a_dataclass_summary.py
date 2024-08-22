import json
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Student:
    name: str
    math: int = 0
    english: int = 0
    science: int = 0
    history: int = 0
    comment: str = ""
    report_count: ClassVar[int] = 0

    def __post_init__(self):
        Student.report_count += 1

    def get_subjects(self):
        return ['math', 'english', 'science', 'history'] 

    def calculate_average(self):
        return (self.english + self.science + self.history + self.math) / 4

    def generate_summary(self):
        above = 0
        scores = [self.math, self.english, self.science, self.history]
        subjects = self.get_subjects()
        avg = self.calculate_average()
        for score in scores:
            if score > avg:
                above += 1
        best = subjects[scores.index(max(scores))]
        print(f"""
Student Name: {self.name}

Math: {self.math}
English: {self.english}
Science: {self.science}
History: {self.history}

{self.name} has excelled at {best.capitalize()} and achieved an average grade of {avg:.2f}.
{self.name} performed above average on {above} of 4 subjects.
{self.comment}

------------------------""")

students = []
with open('resources/reports.json') as jsonfile:
# with open('reports.json') as jsonfile:
    info = json.load(jsonfile)
    for item in info['reports']:
        students.append(Student(**item))
 
print(f"Number of reports loaded: {Student.report_count}")
for student in students:
    student.generate_summary()