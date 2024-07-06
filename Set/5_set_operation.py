set_parent = {1, 2, 33, 10, 44, 20, 22, 55}
set_1 = {1,2,33,44,55,22}
print(set_1)

set_2 = {10,20,10,22,55}    #output: {10, 20, 22, 55}
print(set_2)

set_3 = {1,2,33}        # a subset of set_1

set_1.add(10)
print(set_1)
set_1.add(10)       # set does not allow to add duplicate item

print(set_1)


set_2 = {10,20,10,22,55}    #output: {10, 20, 22, 55}
print(set_2)
set_2.remove(10)
print(set_2)        # output: {20, 22, 55}

# find difference in both set
print(set_1.difference(set_2))      # output: {1, 2, 33, 10, 44} method: A/B
print(set_2.difference(set_1))      # output: {20}  method: B/A

# find common item
print(set_1.intersection(set_2))    #output: {22,55}

# find union
print(set_1.union(set_2))       #output: {1, 2, 33, 10, 44, 20, 22, 55}
 
# check if supper set   --- To check wether a set is parent set of another set or not.
print(set_1.issuperset(set_2))  # output: False.
print(set_2.issuperset(set_1))  # output: False.
print(set_parent.issuperset(set_1))  # output: True.
print(set_parent.issuperset(set_2))  # output: True.

# chek if subset [set_3 = {1,2,33}]
print(set_3.issubset(set_1))        # output: True
print(set_1.issubset(set_parent))   # output: True
print(set_2.issubset(set_parent))   # output: True
print({1,2}.issubset(set_parent))   # output: True
print({1,39}.issubset(set_parent))  # output: False
