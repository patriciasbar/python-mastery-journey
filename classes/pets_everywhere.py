class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals
    
    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around."
    

class Simon(Cat):
    def sing(self, sounds):
        return f"{sounds}"
    

class Sally(Cat):
    def sing(self, sounds):
        return f"{sounds}"
    

class Gigi(Cat):
    def sing(self, sounds):
        return f"{sounds}"

my_cats = []  
simon = Simon('Simon', 3)
sally = Sally('Sally', 4)
gigi = Gigi('Gigi', 1)

my_cats.append(simon)
my_cats.append(sally)
my_cats.append(gigi)

my_pets = Pets(my_cats)
print(my_pets.walk())

#introspection
print(dir(my_pets))


