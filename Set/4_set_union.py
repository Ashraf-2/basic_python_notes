set_1 = {1,2,3,4,5}
set_2 = {1,2,33,44,55}
print("intersection item: ",set_1 & set_2)  # method: (A n B)
print("union item of set: ", set_1.union(set_2))    # method: (A u B)
print("unique value of set item: ", set_1 ^ set_2)      # method: U - (A n B)
set_3 = {1,2,3,5}       # checking subset
print(set_3.issubset(set_1))