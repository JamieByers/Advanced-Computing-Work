class Person: 
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    def showPerson(self):
        print(self._name)
        print(self._age)

class Employee(Person):
    def __init__(self, name, age, empID, salary):
        super().__init__(self, name, age)
        self.empID = empID
        self.salary = salary

    def showEmployee(self):
        super().showPerson(self)
        print(self.empID)
        print(self.salary)

p = Person("Stuart", 16)
e = Employee("Adi", 16, "eawdwdfawf", 15600)

p.showPerson()
e.showEmployee()
