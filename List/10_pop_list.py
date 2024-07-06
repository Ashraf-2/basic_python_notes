fruits = ["amm", "jaam", "kathal", "lechu", "anarosh"]
print(fruits)       # output: ['amm', 'anarosh', 'jaam', 'kathal', 'lechu']
     
last_item = fruits.pop()     #it returns the last item of the list and remove it from the list.
print(last_item,"--",fruits)

# even we can give index to remove an item.

fruits.pop(1)       # output: ['amm', 'kathal', 'lechu']
print(fruits)