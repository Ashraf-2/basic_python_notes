words = "Hill side fly"

new_words = list(words)
print(new_words)
i = 0

while i < len(new_words)-1:
    if(new_words[i] == " "):        #avoiding spaces so that not to change it's index
        i+=1
        continue
    else: 
        new_words[i], new_words[i+1] = new_words[i+1], new_words[i]
        i+=2

changed_indecises = "".join(new_words)
print(changed_indecises)