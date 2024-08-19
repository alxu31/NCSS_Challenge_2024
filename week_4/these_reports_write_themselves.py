class Student:
  def __init__(self, name, maths, english, science, history):
    self.name = name
    self.comment = ""
    self.maths = maths
    self.english = english
    self.science = science
    self.history = history

  def calculate_average(self):
    self.average = (self.maths + self.english + self.science + self.history)/4
    return self.average

  def print_report(self):
    print(f"""Name: {self.name}
Math: {self.maths}
English: {self.english}
Science: {self.science}
History: {self.history}
Average: {self.calculate_average():.2f}
------------------------""")

if __name__ == '__main__':
  students = [
    Student('Alice', 85, 92, 88, 95),
    Student('Bob', 70, 80, 75, 85),
    Student('Charlie', 90, 88, 92, 82),
    Student('Diana', 95, 90, 88, 92)
  ]
  for student in students:
    student.print_report()