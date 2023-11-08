from persona import Person
class Teacher(Person):
    def __init__(self,name,surname,age):
        Person.__init__(self, name, surname, age)
        self.subjects = []

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age}, teacher"

    def subjects_list(self):
        return self.subjects

    def add_subjects(self, subject_name):
        self.subjects.append(subject_name)