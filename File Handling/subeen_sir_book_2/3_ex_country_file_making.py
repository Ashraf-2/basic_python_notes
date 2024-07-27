# TASK: Read a file having name of countries and find out which country name starts with "A" and "B" and add to the particular List of the matched alphabatical order.

A_country_name = []
B_country_name = []
others_country_name = []

word_string = ""    #empty string
with open("country_name.txt","r") as fp:
    list_country_name = fp.read().split(",")   #remove "," and  make a list of name of the countries.
    # print("file list: ",list_country_name)
    for name in list_country_name:
        if(name.strip().upper()[0] == "A"):     # check if the the name starts with "A"
            A_country_name.append(name.strip())  ## by removing whitespace from tail and start and added to list
        elif(name.strip().upper()[0] == "B"):   # check if the name starts with "B"
            B_country_name.append(name.strip())    # by removing whitespace from tail and start and added to list
        else: 
            others_country_name.append(name.strip())


# Taks-2: now store the name of "A" starting country in "a.txt" file and store the name of "B" starting country in "b.txt".
with open("b.txt","w") as fp:
    for word in B_country_name:
        fp.write(word+"\n")



with open("a.txt","w") as fp:
    for word in A_country_name:
        fp.write(word+"\n")



print("Country Name with A: ",A_country_name, len(A_country_name))
print("Country Name with B: ",B_country_name, len(B_country_name))
print("Others country name: ",others_country_name, len(others_country_name))
