class Student:

    student_grades: list[float] = []
    def __init__(self, name: str, grade: float, gradel: list):
        self.name: str= name
        self.grade: float = grade
        self.student_grades.append(grade)
        self.my_grades: list= gradel

    def print_grade(self):
        print(f'il mio voto è {self.grade}')

    def grades_average(self):
        return sum(self.my_grades) / len(self.my_grades)

    @classmethod
    def get_avg_grades(cls) -> float:
        avg = sum(cls.student_grades)/ len(cls.student_grades)
        return avg
    
francesca = Student(grade=9, name='Francesca', gradel=[9,7,8,5])
print(Student.student_grades)
bardh = Student( name= 'Bard', grade=6)
print(Student.student_grades)
bardh.print_grade()
francesca.print_grade()
print(francesca.grades_average)

avg = Student.get_avg_grades()
print(f'la media dei voti è {avg}')
