from datetime import date

Professors = []

class Professor():

    def __init__(self, name:str ,professor_id:int, date_register: date):
        self.professor_id = professor_id
        self.name = name
        self.date_register = date_register

    @property
    def ID(self):
        return self.professor_id
    
    @property
    def Name(self):
        return self.name

    @property
    def Date_register(self):
        return self.date_register

    def Antiquity(self, antiquity):
        self.antiquity = antiquity
        pass

    @Name.setter
    def Name(self, value):
        self.name = value
    
    @Date_register.setter
    def Date_register(self, value):
        self.date_register = value

prof = Professor('Alfonso Gutierrez', 12358, (2019,3,21))
Professors.append(prof)

    
        