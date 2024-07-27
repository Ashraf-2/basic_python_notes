import datetime
x = datetime.datetime.now()
print(x)
stx = " "+ str(x)
f = open('myfile1.txt','w')
f.write('This file is created using python now at')
f.write(stx)