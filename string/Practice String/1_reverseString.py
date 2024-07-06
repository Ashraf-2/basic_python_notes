# Write a program that takes a string as input and prints it in reverse.

# text = input("Write something: ")
text = "boss"
# print(text)
index = len(text)-1
print(index)
while(index>=0):
    print(index," - ",text[index])
    index -=1

# another way

# Get input from the user
text = "beng"

# Reverse the string using slicing
reversed_text = text[::-1]

# Print the reversed string
print("Reversed text:", reversed_text)
