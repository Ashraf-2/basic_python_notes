def myfunc(numbers):
    for i in range(len(numbers)):
        print(numbers[i])
    numbers[2]=100
num1 = [1,2,3,32,4]
myfunc(num1)
print(num1)
# inside of a function, list is mutable and can change it's value like a global value.