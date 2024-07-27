# Task: write a program that counts the number of vowel in a string.

vowels = ['a','e','i','o','u']
vowels_length = len(vowels)
text = "Hello world, We are here!"
count = 0

# for i in range(len(text)):
    # print(text[i])

for i in range(vowels_length):
    for j in range(len(text)):
        if(vowels[i] == text[j]):
            count +=1
        j+=1
    i+=1
print("numbers of vowerl in text: ",count)    
