#create class

class Car():

    #class attribute
    max_speed = 120     # km /h 

    # constructor
    def __init__(self,brand, model, color, speed=0):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = speed      # initial speed = 0

    # method for accelaration
    def accelerate_car(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed = self.speed + acceleration 
        else:
            self.speed = Car.max_speed      # if driver tries to exceed the limit.
    # method to get current speed
    def current_speed(self):
        return self.speed
    
# create instances
car1 = Car("Blush","B17","RedWine")

car1.current_speed()        # initially = 0
car1.accelerate_car(82)     # speed up to = 82
print("current speed of",car1.brand, car1.model, "is :",car1.current_speed(),"km/h") # speed = 82