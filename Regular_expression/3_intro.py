import re

s = "bangladesh"
match = re.search(".",s)
print(match.group()) # output: b
match = re.search("..",s)
print(match.group()) # output: ba
match = re.search("b.n",s)
print(match.group()) # output: ban
match = re.search("..........",s)
print(match.group()) # output: bangladesh