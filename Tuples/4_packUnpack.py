tuple1 = (1,33,2,545,23)
tuple_sort = sorted(tuple1)
print(tuple_sort)       # output: [1, 2, 23, 33, 545]   #also it becomes a list
print(type(tuple_sort))
n1, n2, n3, n4, n5 = tuple_sort     #you can not unpack tuple's item less then of it total item.
# impossible: n4, n5 = tuple_sort 
print(n1, n2)   # output: 1 2

new_tuple = n1, n2,n3
print(new_tuple)    # output:(1, 2, 23)