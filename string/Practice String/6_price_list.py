# print the items and price list like a billing machine output using dictionary and ljust and rjust method

price_dict ={
    "Pen": 6,
    "Notepad": 14,
    "iPad": 650,
    "Books": 220
}
print("\n")
print("Price List".center(20,"-"))
r_just, l_just = 4,12
# print(r_just,l_just)
sum = 0
for k , v in price_dict.items():
    print(k.ljust(l_just,"-"),str(v).rjust(r_just," "))
    sum +=v
print("_".center(20,"_"))
print("Total".ljust(12,"-"), str(sum).rjust(r_just,(" ")))