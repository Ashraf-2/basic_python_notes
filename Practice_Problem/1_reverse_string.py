# Task: write a program that takes a string and returns it reversed.

str1 = "Hello Word"

words_list = str1.split()

length_words_list = len(words_list)

words_list = words_list[::-1]
print(words_list)
reversed_string = " ".join(words_list)
print(reversed_string)


# for i in range(length_words_list):