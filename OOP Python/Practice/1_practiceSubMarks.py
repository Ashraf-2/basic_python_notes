# Credit: Shraddha Didi (youtube)
# create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:

    def __init__(self,name, list_of_marks):     #constructor
        self.name = name
        self.marks = list_of_marks
    
    def get_avg_marks(self):        #method
        sum = 0
        for value in self.marks:
            sum = sum + value
        avg = sum/3
        print(self.name,", your average score is", avg)
        return avg
    
    # static method - on class level
    @staticmethod       #decorator
    def hello():
        print("hello student!")

s1 = Student("karima",[12,23,34])
print(s1.marks)
s1.name = "Shraddha"        # manipulate the attribute
# s1_avg_marks = s1.get_avg_marks()
print(s1.get_avg_marks())
s1.hello()
        