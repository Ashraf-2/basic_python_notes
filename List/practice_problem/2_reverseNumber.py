# problem - 6
# reverse the integer number
# 1342 -> 2431
 
a = int(input("number: "))

len = len(str(a))
rev_a = 0
for i in range(len):
    last_digit = a%10
    rev_a = rev_a*10 + last_digit
    a = a // 10

print("reverse number: ", rev_a)