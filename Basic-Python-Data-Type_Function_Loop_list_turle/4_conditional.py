
bd1 = "bangladesh"
bd2 = "bangladesh2"
if(bd1==bd2):
    print("same case is used")
else: 
    print("spelling but Different case is used")

number1 = float(input("Number: "))
setNumber = 100

if(number1>=0 and number1<100):
    print("This is bellow hundred")
elif(number1<0):
    print("Invalid Number!")
elif(number1>100):
    print("Out of reach!")
else:
    print("Payment successfull $100")