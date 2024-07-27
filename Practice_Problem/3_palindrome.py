# Task: Write a program to check if a string is a palindrome.

text = "Ashraful"
# text = "NOYON"
def check_palindrom(text_p):
    index = len(text_p)-1
    i=0 
    while(i<=(len(text_p)//2)):
        if(text_p[i] != text_p[index]):
            return -1
        else:
            i+=1
            index-=1
            continue
        return 1
palindrome_status = check_palindrom(text)
if(palindrome_status == -1):
    print("this is not a palindromic text")
else:
    print("this is a palindromic text")