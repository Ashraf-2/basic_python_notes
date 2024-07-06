numbers = [13,2345,12,1,234,19,0.2,10000]

max_number = numbers[0]
for i in numbers:
    if i>max_number:
        max_number = i
print("max value: ", max_number)

min_number = numbers[0]
for i in numbers:
    if i<min_number:
        min_number = i
print("min value: ", min_number)

x = max(numbers)
y = min(numbers)
print(x,y)

