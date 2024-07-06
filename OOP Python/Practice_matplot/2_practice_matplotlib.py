
import matplotlib.pyplot as plt

class Circle:
    # constructor
    def __init__(self, radius=3, color="blue"):
        self.radius = radius
        self.color = color
    
    # method 
    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)
    
    # method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0),radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

# creating instances
RedCircle = Circle(10,'red')
dir(RedCircle)
print(RedCircle.radius)
print(RedCircle.color)

# RedCircle.drawCircle()

RedCircle.add_radius(2)
RedCircle.drawCircle()
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)

# blue circel instance
BlueCircle = Circle(3,"blue")
print(BlueCircle.radius)
print(BlueCircle.color)
print(BlueCircle.drawCircle())