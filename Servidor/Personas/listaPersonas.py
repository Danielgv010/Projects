#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

from persona import Person
from alumno import Student
from profesor import Teacher


print("Content-type: text/plain\n")

person1 = Person("Juan","Rodriguez García",33)

print(f"{person1.name} {person1.surname}")

person2 = Person("Ana","López García",43)

person2.alive = False

if (person2.alive):
    print(f"{person2.full_name()}")
else:
    print("RIP")

print(person2)

student1 = Student("Jose","García García", 18, "DAW")
print(student1)
print(student1.grade_name())

teacher1 = Teacher("AAAA","BBBB CCCC",50)
teacher1.add_subjects("Servidor")
teacher1.add_subjects("Cliente")

print(teacher1)
for subject in teacher1.subjects_list():
    print(subject)