# Task: Write a program that takes a sentence and returns the sentence with each word reversed.

text = "Hello programmar! How's going on? Welcome to the world of code :)"

# split the sentence into individual word.
words = text.split()

# print(words)

reversed_word_list = []     #create an empty list for the newly created list of teh reversed words.

for word in words:
    # way-1:

    # reverse each word
    word = word[::-1]
    # print(word)
    reversed_word_list.append(word)     # list of reversed words 
    # way-2:
    # reversed_word_list.append(word[::-1])
# print(reversed_word_list)

# now join the each of reversed word to make a complete sentence
sentence_of_reversed_words =" ".join(reversed_word_list)
print(sentence_of_reversed_words)





'''
Solutions:
1. split the words into and make a list.
2. make reverse of each words of the list.
3. create an empty list.
4. add all the reversed word (of step 2) into the newly created empty list (in step 3)
5. now join the words of the reversed list to make a sentece.

---Yeeehhh....You solved it!!----
'''