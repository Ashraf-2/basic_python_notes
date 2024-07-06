# Credit: Shraddha Didi (youtube)
# abstruction

class Car:
    def __init__(self):
        self.accelarator = False
        self.brake = False
        self.cluth = False

    def start(self):
        self.accelarator = True     # abstruction - work internally
        self.cluth = True           # abstruction - work internally.
        print("Engine Starts..")

car1 = Car()
car1.start()