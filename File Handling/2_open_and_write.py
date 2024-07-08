# open the file

f = open('sample_txt1.txt', 'w')
f.write('This text added now using python!')        # it will delete all existing lines and add this line only.
f.close()

# reopen the file
rf = open('sample_txt1.txt','r')
print(rf.read())
rf.close()
