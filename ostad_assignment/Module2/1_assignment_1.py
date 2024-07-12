'''
Taskl: Write a program to make another list of duplicate elements from the following list
[1, 5, 6, 5, 1, 2, 3]

'''

list1 = [1,5,6,5,1,2,3]
list_unique = []
list_duplicate = []

for i in list1:
    if not i in list_unique:
        list_unique.append(i)
    # print(i)
    else:
        list_duplicate.append(i)

print(list_duplicate)       # output: [5,1]
print(list_unique)          # output: [1,5,6,2,3]

# another way
'''
original_list = [1, 5, 6, 5, 1, 2, 3]

# Initialize a set to track seen elements
seen = set()
# Initialize a list to store duplicate elements
duplicates = []

# Iterate through the original list
for element in original_list:
    # Check if the element has been seen before
    if element in seen:
        # If it is a duplicate, add it to the duplicates list if not already added
        if element not in duplicates:
            duplicates.append(element)
    else:
        # If it is not a duplicate, add it to the seen set
        seen.add(element)

print("Duplicate elements:", duplicates)

'''