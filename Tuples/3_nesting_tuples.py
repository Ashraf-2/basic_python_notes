tuple1 = (1,2,('one','two'),(4,5),("disc","bullet",(22,33)))
print(tuple1)       # output: (1,2,('one','two'),(4,5),("disc","bullet",(22,33)))
print(len(tuple1))     # output: 5
print(tuple1[2])        # output: ('one', 'two')
print(tuple1[2][0])     # output: one
print(tuple1[2][1])     # output: two
print(tuple1[4][2][1])     # output: 33

tuple2 = (1,2,3,["one","two"],[1.2,5.3])
print("big tuple: ", tuple2)