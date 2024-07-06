jhon = "5"
print(jhon)

x=5
y=2.4
print(x+y)

print(type("Lekha"))
print(type(x))
print(type(y))
print(type(5+2.4))

#assign multiple variables

a,b,c = 2,"two","hello"
print(a,"-",b,"-",c)
print(type(a),type(b),type(c))

#assign same value in multiple variables

aa=bb=cc="same"
print(cc)
if(aa==bb==cc):
    print("true, these are same")
cc="changed"
print(aa,bb,"after change: ",cc)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#variable scope:
x = "awesome1"

def myfunc():
  x="Dark"
  print("Python is " + x)

#global variable:
def fun2():
  global x
  x = "fantastic"

fun2()

print("Python is " + x)
 
print(x)