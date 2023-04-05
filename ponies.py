''' File for creating the poney class'''

class Poney:

    # All ponies begin with a unique name and variable starting speed
    def __init__(self, name, location = 0, speed = 3):

        self.name = name
        self.location = location
        self.speed = speed

    def say_name(self):

        print(f"My name is {self.name}.")


    def say_location(self):

        print(f"I am at {str(self.location)} location.")


    def say_speed(self):

        print(f"I am going {self.speed} fast!!!")


    def change_speed(self, change):

        self.speed += change

        return self.speed
    
    def move(self):

        self.location += self.speed


