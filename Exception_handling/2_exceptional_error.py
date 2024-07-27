def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Can't divide by Zero")
    except TypeError:
        print("Unsupported data type. Please use numeric.")

print(div(1,2))
print(div(100,2))
print(div(10,2))
print(div(1,0))
print(div("fb",3))

