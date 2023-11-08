class Person:
    def __init__(self,name,surname,age): # Constructor, self siempre como primer parámetro
        self.name = name
        self.surname = surname
        self.age = age
        self.alive = True

    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self): # Accede aqui cuando se llama al objeto sin metodo
        return f"{self.name} {self.surname}, {self.age}"