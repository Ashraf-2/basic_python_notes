#write a program that will replace the 1st index and 2nd index, 3rd and 4th, 5th and 6th and until the last index.
def change_index(word):
    length = len(word)
    new_word = list(word)  # Convert the string to a list to allow modifications
    i = 0
    while i < length - 1:
        # Swap the characters at index i and i+1
        
        new_word[i], new_word[i + 1] = new_word[i + 1], new_word[i]
        i += 2  # Move to the next pair of indices
    return ''.join(new_word)  # Convert the list back to a string

st = "bangladesh fly"
print(st)

changed_word = change_index(st)
print(changed_word)
