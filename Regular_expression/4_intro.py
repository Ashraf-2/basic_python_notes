import re
s = "bangladesh is our homeland"
match = re.search("o\w\w",s)
print(match.group())    # output: our
match = re.search("o\w\w\w\w",s)
print(match.group())    #output: omela
match = re.search('b\w+h',s) # output: bangladesh
print(match.group())