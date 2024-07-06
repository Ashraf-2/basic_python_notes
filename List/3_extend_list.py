l1 = [2,3,4,14,"hello"]
l2 = ["bro",33,55]
l1.extend(l2)       #extend list l2 with l1 and it only added  list items. not an entire list.


print(l1)
l2.extend([99, "watch", "belt"])
print(l2)