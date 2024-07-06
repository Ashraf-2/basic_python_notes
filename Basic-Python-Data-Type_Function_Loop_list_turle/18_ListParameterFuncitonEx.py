# write a program that will take a parameter as a list and return the average of the list numbers values.

def find_average(numbers):
    # summ=0
    # for i in range(len(numbers)):
    #     summ +=numbers[i]
    summ = sum(numbers)
    average = summ/len(numbers)
    return average

num1= [10,20,40,50]
print("average of the list numbers: ",find_average(num1))