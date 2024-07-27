# Use try except to ignore a particular type of error and let continue your program to run.


def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Math error.\nYou tried to divide a number by Zero.")
        return None

print(div(12,3))
print(div(44,4))
print(div(0,100))
print(div(33,4))
print(div(33,0))
print(div(100,5))
