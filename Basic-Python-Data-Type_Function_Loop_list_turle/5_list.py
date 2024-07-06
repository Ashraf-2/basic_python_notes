numbers = [1,32,32,3,43,1,21]
print(type(numbers))
print(numbers)

sorted(numbers) #does not manipulate parent list items.
print("Numbers: ",numbers)
sorted_numbers = sorted(numbers)     #sorted numbers will be assign in new variable.
print("Sorted Numbers: ",sorted_numbers )

if (numbers == sorted_numbers):
    print("Manipulated")
else:
    print("Parent list never manipulate")

print(numbers[0])
print(numbers[2])
print(sorted_numbers[0])
print(sorted_numbers[2])

length_numbers = len(numbers)
print("length of the numbers list: ",length_numbers)
print("last degit of the list: ",numbers[len(numbers)-1])