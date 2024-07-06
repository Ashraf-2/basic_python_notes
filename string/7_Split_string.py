#split() method is used to make split in a big a string to create a lot of new smaller strings.
#split() method convert a string into a "List" having all of its all smaller part
text = "Hello programmer, Python is a beginner friendly general purpose language"

new_split = text.split()
print(text)
print(new_split)
print("0 ----",new_split[0],",","3 ------",new_split[3] )
len_of_new_split = len(new_split)
print("length of new splitted sentence: ",len_of_new_split)
last_word = new_split[len_of_new_split-1]
print(last_word)