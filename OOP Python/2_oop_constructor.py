# Credit: Shraddha Didi (youtube)
class Student:

    # defaulf constructor
    def __init__(self):
        pass
    
    # creating parameterized constructor
    def __init__(self, fullname, marks):       # self always should be passed and it should be at the first position.
        # print(self)
        self.name = fullname        # attributes
        self.marks = marks
        print("adding new student in database...")

s1 = Student("Khadim",92)
print(s1.name, s1.marks)

s2 = Student("Mahim",83)
print(s2.name, s2.marks)
