#list is mutable. you can add, remove, manipulate list items
list1 = [1,2,3,4,5,5,6,"hello",True]
print(list1)    # Output: [1, 2, 3, 4, 5,5, 6, 'hello', True]
list1.remove("hello")
print(list1)    # Output: [1, 2, 3, 4, 5,5, 6, True]
print(len(list1))
print(list1.count(5))    # Output: 2
list1[2] = "third_index"
print(list1)    # Outpu: [1, 2, 'third_index', 4, 5, 5, 6, True]
# Tuples is Immutable. it's work like list but it is not changable like list.

# list start using [], and tuple start using ()

tuple1 = (1,2,3,1,4,5,"hello",False,0.23)
print("tuple1: ",tuple1)       # Output: (1, 2, 3, 4, 5, 'hello', False)
print(len(tuple1))
print(tuple1.count(1)) # Output:2
# tuple1[0] = "one"     #impossible to manipulate the item in tuple

