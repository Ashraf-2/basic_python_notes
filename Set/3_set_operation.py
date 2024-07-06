# intersection and union in set

A = {1,2,4,5}
B = {100,10,2, 20}

C = A & B       # "&" means intersection
print(C)        # output: {2}

D = A | B       # " | " mean union
print(D)

E = A - B       # set substrection: only the value which belongs to only in "A", not included any common value
print(E)    # output: {1, 4, 5}

F = B - A       # output: {10, 100, 20} , only the value which included in only B, not included any common value
print(F)

G = A ^ B       # only the unique value in both A and B set belongs to. but not included any common value.
print(G)         # output: {1, 100, 4, 5, 10, 20}
