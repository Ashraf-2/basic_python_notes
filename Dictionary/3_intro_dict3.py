dt = {}
print(dt)
print(type(dt))
dt[1] = "pen"
dt[2] = "book"
print(dt)       # output: {1: 'pen', 2: 'book'}
dt[(3)] = "three"
print(dt)

# another example

dt[(4,5,6)]= 92
print(dt)       # output: {1: 'pen', 2: 'book', 3: 'three', (4, 5, 6): 'four five six'}

# li = [11,22,34]       # unhashable type in dictionary. Not posssible.
# dt[li] = "Hello"
# print(dt)

# NOTE: you can use anything as KEY which is not mutable. Like: you should avoid List and Set, as they are mutable data struture.

print(dt[3])
print(dt[(4,5,6)])