# Credit: Shraddha Didi (youtube)
class Car:

    brand = "Blush"     # class attribute
    model = "Annonymous"    # class attribute
    def __init__(self,model, color):
        self.model = model       # object attribute
        self.color = color
    def welcome (self):     # method
        print("Welcome in my Store to buy",self.brand)
    def get_model(self):    # method
        return self.model
    
# when class attribute and object attribte is same that moment if you pass the object attribute then object attribute will work, otherwise the class attribute will work
car1 = Car("DH116", "Blue")
print(car1.model, car1.brand)   # output: DH116 Blush
print(Car.brand)        # output: blush

car2 = Car(model="DH118", color="Yellow")
print(car2.brand, car2.model, car2.color)       #output: Blush DH118 Yellow
car1.welcome()
print(car1.get_model())
