"""
with open("example.txt","r") as fp:
    lines = fp.readlines()
    for line in lines:
        print(line)
"""

with open("example.txt","r") as fp:
    print(fp.read())