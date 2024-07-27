# Task: open a file using "with" and count the frequency of word of that file.


with open('sample_txt1.txt','r') as file1:
    content = file1.read()
# this file will automatically close after the "with" block
# print(content)
formatted_text = content.replace('.','').replace(',','')
# print(formatted_text)
wordsList = formatted_text.split()
counter_dict = {}
for word in set(wordsList):
    counter_dict[word] = wordsList.count(word)
print(counter_dict)

file1.close()

print(content)