list1 = [1,2,3,4,5,2,5,23]
list1.sort()
print(list1)
print(23 in list1)      # output: true
print(22 in list1)      # output: false
if(1 in list1):         # output: 1 ache re bhai ache
    print("1 ache re bhai ache!")           
else:
    print("dur mia, vhua number den ken!")