# problem -1
# find out armstrong number ?
# 153 = 1^3 + 5^3 + 3^3 = 153 ----> it is an armstrong number

# method - 1

a = int(input("Number: "))
num_len = len(str(a))       #number of digit
temp = a
sum = 0
while(temp>0):
    last_digit = temp%10        #getting last digit
    sum = sum+last_digit**num_len
    #temp = temp // 10
    temp //= 10

if(sum == a):
    print("it is an armstrong number")
else:
    print("Not armstrong")

#method -2 
a = input("number please: ")
num_len2 = len(a)
sum=0
for i in a:
    sum = sum + int(i)**num_len2
if(int(a) == sum):
    print("armstrong number")
else:
    print("not armstrong")