sarc= ['Bangladesh',"India","Bhutan","Nepal","Afganistan"]
print(sarc,",length: ",len(sarc))
print("bd" in sarc)
print("ABC" in sarc)
print("ABC" not in sarc)

country = input("Country: ")
if(country in sarc):
    print(country,"is a member of SARC")
else:
    print(country,"is not a member of SARC")