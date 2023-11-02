from persona import Person

class Student(Person):
    def __init__(self,name,surname,age,grade):
        Person.__init__(self,name,surname,age) # Hay que pasarle el self para hacer la herencia
        self.grade = grade

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age}, {self.grade}"

    def grade_name(self):
        return f"Está estudiando {self.grade}"