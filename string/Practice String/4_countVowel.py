# Write a program to count the number of vowels in a given string.
vowels = ['a','e','i','o','u']

text = input("text: ")

number_of_vowels = 0
# print(len(vowels))
for i in range(len(vowels)):
    for x in range(len(text)):
        if(vowels[i] == text[x]):
            number_of_vowels +=1
        else:
            continue

print(number_of_vowels)
