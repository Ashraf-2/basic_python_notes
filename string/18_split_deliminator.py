str1 = "A,B,C,D"
str2 = str1.split(",")      #it make the string into a list and split all item using the deliminator
str3 = str1.split("-")      #it make the string into a list and but not split all item using the deliminator, because the deliminator does not exist in str1.
print(str1)
print(str2)
print(str3)