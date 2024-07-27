string = "Hello"
print(string.rjust(10))  # output:     Hello
print(string.ljust(10))  # output:Hello
print(string.rjust(10,"-"))  # output:-----Hello
print(string.ljust(10,"@"))  # output:Hello@@@@@
print(string.ljust(10,"*"))  # output:Hello*****

print(string.center(20)) # output:        Hello
print(string.center(20,"^")) # output: ^^^^^^^Hello^^^^^^^^