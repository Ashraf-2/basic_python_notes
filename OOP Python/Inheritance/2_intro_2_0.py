"""Creating Parent Class and Child Class and work on them"""

class Vehicle:  # parent class
    """Base (parent) class for all type of vehicles"""

    def __init__(self,name, manufacturer, color) :
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
    
    def drive(self):
        print("Driving",self.manufacturer,self.name)
    
    def turn(self,direction):
        print("Turning",self.name,"to",direction)

    def brake(self):
        print(self.name,"is stopped!")

if __name__ == "__main__":
    # creating instances of Vehicle class
    v1 = Vehicle("Black Dragon 78","Marcedezh","Red")
    v2 = Vehicle("White Stone 93","RedCorxx","White")
    v3 = Vehicle("Softail Delux 53","Harley-Davidson","Blue")

# calling method.
v1.drive()
v2.drive()
v3.drive()

v1.turn("80 degree left")
v2.turn("Right")

v1.brake()
v2.brake()

# create child class

class Car(Vehicle): #child class of Vehicle class.
    wheel = 4  # object attribute 
    
    
    # creating constructor for Car class
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color)     # inheritting attribute of it's parent class
        self.year = year
        print("- A new car has been enlisted today, Name:",self.name)
        print("- It has",self.wheel,"wheel")
        print("- The car is build in the year",self.year)    
    # method of Car class
    def change_gear(self, gear_name):  # a method to change gear
        print(self.manufacturer, self.name, "is changed gear to", gear_name)

# create instances
c1 = Car("Vostock","Martinia","Yellow", 2025)
# print(c1.color) # attribute
print(c1.name) # attribute
print(c1.year) # attribute
# calling the method
c1.change_gear("MenoMax") # own method
c1.brake() # inheritting brake method from its' parent class 



