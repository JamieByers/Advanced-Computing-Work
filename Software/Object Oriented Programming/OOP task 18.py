class Dog:

    def __init__(self, name, age, breed) -> None:
        self.name = name 
        self.age = age 
        self.breed = breed 
        self.friendsArray = []

    def display_dog_info(self):
        print(self.name, "is a ", self.breed, "and is ", self.age, "years old")
        if self.friendsArray:
            print(f"here are {self.name}'s friends")
            for friend in self.friendsArray:
                print(friend.name)

    def addFriend(self, ob):
        self.friendsArray.append(ob)
        ob.friendsArray.append(self)

