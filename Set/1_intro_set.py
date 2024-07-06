A = set()
print(A)
print(type(A))

AB = {1,2,3,34,"pen","book",("hello","hi")}
print(AB)
# NOTE: set does not maintain order.
for i in AB:
    print(i)
print("length of set AB: ", len(AB))

print("pen" in AB)      # output: True