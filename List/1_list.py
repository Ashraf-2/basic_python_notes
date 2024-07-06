L = [ "Michael Jackson", 10.2]
print(L)
print(len(L))

for i in range(len(L)):
    print(i)

L2 = L
print(L2)
L2.append('bro')        #it also change the parent List 'L'. cause list keeps the reference.
print(L2, L)    

l3 = L[:]       # this is called "clone the list without keeping reference" 
print(l3)       
l3[2] = "sis"
print(l3, L)

l4 = []
print(l4)
print(len(l4))


#list traversing
print("traversing --- ")
list1 = [2,3,4,5,6,7]
lenght = len(list1)
for i in range(-1, -(lenght+1),-1):
    print(list1[i])

print("anoter way ---")
for i in range(lenght-1, -1, -1):
    print(list1[i])