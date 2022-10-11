from datetime import date

Students = []
class Student:

    def __init__(self, name:str, id:int, date_birth:date, registration_date:date, gender:str, city:str):

        self.name = name
        self.id = id
        self.date_birth = date_birth
        self.registration_date = registration_date
        self.gender = gender
        self.city = city

    @property
    def ID(self):
        return self.id

    @property
    def Name(self):
        return self.name
    @property

    def DateBirth(self):
        return self.date_birth

    @property
    def RegisDate(self):
        return self.registration_date

    @property
    def Gender(self):
        return self.gender

    @property
    def City(self):
        return self.city

    @ID.setter
    def ID(self, value):
        self.id = value
    
    @Name.setter
    def Name(self, value):
        self.name = value
    
    @DateBirth.setter
    def DateBirth(self, value):
        self.date_birth = value
    
    @RegisDate.setter
    def RegisDate(self, value):
        self.registration_date = value
    
    @Gender.setter
    def Gender(self, value):
        self.gender = value
    
    @City.setter
    def City(self, value):
        self.City = value

    def Show(self):
        for students in Students:
            return f'{students.name} / {students.id} / {students.date_birth} / {students.registration_date} / {students.gender} / {students.city}'
            
#Esto no se ejecuta como debería, no llena la lista
    def RegisteredStudent(self):
        student = Student('Alma', 15648, (2002,6,13), (2021,5,21), 'M', 'Tala, Jalisco')
        Students.append(student)
        student = Student('Miguel', 15648, (2002,6,13), (2021,5,21), 'M', 'Tala, Jalisco')
        Students.append(student)
    
student = Student('Miguel', 15648, (2002,6,13), (2021,5,21), 'M', 'Tala, Jalisco')
Students.append(student)

print(student.Show())