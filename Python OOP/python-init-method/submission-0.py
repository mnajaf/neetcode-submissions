class Pet:
    def __init__ (self,name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age


# Don't modify the code below this line
fluffy = Pet("Fluffy", "cat", 3)
buddy = Pet("Buddy", "dog", 2)

print(f"{fluffy.name} is a {fluffy.age} year old {fluffy.species}.")
print(f"{buddy.name} is a {buddy.age} year old {buddy.species}.")
