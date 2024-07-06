# list is mutable and mutation may change it's parent list also.
list1 = [1,2,3,4,5]
list2 = list1
list2[0] = 100

print("list1: ",list1, "list2: ",list2)
