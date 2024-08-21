from dataclasses import dataclass

@dataclass
class Student:
    name: str
    math: int = 0
    english: int = 0
    science: int = 0
    history: int = 0
    comment: str = ""

student1 = Student(name = "Raj", math=91, english=87, science=92, history=78, comment="Excellent performance!")    

if __name__ == "__main__":
    print(f"Here is the report for {student1.name}")      
    print(f"Math: {student1.math}")
    print(f"English: {student1.english}")
    print(f"Science: {student1.science}")
    print(f"History: {student1.history}")
    print(f"Comment: {student1.comment}")
