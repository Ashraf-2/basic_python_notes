lines = [
    "This is first line.",
    "this is second line",
    "this is third line",
    "this is 4th line"
]
#  to write on a file (if the file does not exist then python will create a file and then it will write the file)
with open("file.txt","w") as fp:
    for line in lines:
        fp.write(line+" writing ---\n")
# to read a file
with open("file.txt","r") as fp:
    content = fp.read() # read the whole file at a single moment or at once.
    print(content)

#  to read a file (way-2)
with open("file.txt",'r') as fp:
    lines_read = fp.readlines() # it will read the content of the file line by line.
    print(lines_read)
    for line in lines_read:
        print("x - ", line)

# another way to read the lines
with open("file.txt", 'r') as fp:
    for line in fp:
        print("i - ", line)