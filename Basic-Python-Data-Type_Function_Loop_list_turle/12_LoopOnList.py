alphabet = ['A','B','C','D','E','F','G','H']

for i in alphabet:
    for x in alphabet:
        if(i == x):
            continue
        print(i,x)
#crate list using "range(x)"
li = list(range(11))
print(li)

li2 = list(range(4,21,2))
print(li2)

