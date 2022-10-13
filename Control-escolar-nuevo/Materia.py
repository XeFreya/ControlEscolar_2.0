from Alumnos import Student
from Professor import Professor

class Asignature(Student, Professor):
    def __init__(self, name="", professor="", studentList=list()):
        Student.__init__(self)
        Professor.__init__(self)

        self.name = name
        self.professor = professor
        self.studentList = studentList

    def Add_Student_Asignature(self, student= Student()):
        self.student = student
        pass
    
    def DeteleStudent(self, ID=""):
        self.ID = ID
        pass
