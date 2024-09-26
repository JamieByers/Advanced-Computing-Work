class Dog:
    def __init__(self, name, age, breed) -> None:
        self.name = name 
        self.age = age 
        self.breed = breed 

    def display_dog_info(self):
        print(self.name, "is a ", self.breed, "and is ", self.age, "years old")

    def birthday(self):
        self.age += 1
    
    def bark(self):
        print(self.name, "says woof")


dog = Dog("buddy", 4, "terrier")

dog.display_dog_info()
dog.bark()
dog.birthday()
dog.display_dog_info()