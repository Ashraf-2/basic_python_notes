# class is the blueprint of object.

# class need to create first before creating an object.

# Credit: Shraddha Didi (youtube)

class Student:
    name ="Karan Arjun"

# create object (instances of class)
s1 = Student()
print(s1.name)
# print(type(s1))
# print(type(Student))
s2 = Student()
print(s2.name)



# --- another example ---

class Car:
    color= "blue"
    brand = "mercidiz"
car1 = Car()
print(car1.color)       # output: blue
print(car1.brand)       # output: mercidiz