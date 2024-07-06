#take input of a word and check is it palindrome word or not.

import math
word = input("Write a word: ")


def check_palindrom(word): 
    length = len(word)
    middle_place = math.floor(len(word)/2)
    for i in range(middle_place):
        if(word[i] == word[length-1]):
            length-=1
            continue
        else:
            return False
    return True
    # anoter way
    # for i in range(middle_place):
    #     if word[i] != word[length - i - 1]:
    #         return False
    # return True
palindrom = check_palindrom(word)
if(palindrom):
    print('It is a palindrom word')
else:
    print('It is not a palindrom word')