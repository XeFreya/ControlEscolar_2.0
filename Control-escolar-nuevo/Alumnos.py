from datetime import date

Students = list()
class Student:

    def __init__(self, name="", id="", date_birth="", registration_date="", gender="", city=""):

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
        self.city = value
            
    def AddStudent(self,):
        student = Student()
        print('To add a student to the list of students, please enter the following information: ')
        student.name = input('Name: ')
        student.id = int(input('ID: '))
        print('\nDate birth: ')
        year = int(input('Year: '))
        month = int(input('Month:'))
        day = int(input('Day: '))
        student.date_birth = date(year, month, day)
        print('\nDate of the registration: ')
        year = int(input('Year: '))
        month = int(input('Month: '))
        day= int(input('Day: '))
        student.registration_date = date(year, month, day)
        student.gender = input('Gender (M/F): ')
        student.city = input('City: ')
        Students.append(student) 

    def Show(self):
        print('Name |\t ID |\t Date Birth |\t Registration Date |\t Gender |\t City')
        for students in Students:
            print (f'{students.name} \t {students.id} \t {students.date_birth} \t {students.registration_date} \t\t   {students.gender} \t {students.city}')


student_ = Student('Alma', 154, (2002,6,13), (2021,5,21), 'M', 'Tala, Jalisco')
Students.append(student_)
student_ = Student('Miguel', 15648, (2002,6,13), (2021,5,21), 'M', 'Tala, Jalisco')
Students.append(student_)



# student = Student()
# Students.append(student)
# op = 1
# while op != 0:
#     print('1. Add Student')
#     print('2. Show Student')
#     op = int(input('Enter an option of the following sentences: '))

#     if op == 1:
#         student.AddStudent()
#     elif op == 2:
#         student.Show()