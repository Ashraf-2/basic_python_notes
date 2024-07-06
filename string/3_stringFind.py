country = "bangladesh"
find_ban = country.find("ban")  #find from the first apperance index of "ban"
find_la = country.find("la")    #find from the first apperance index of "la"
print(find_ban,find_la)
find_na = country.find('na')        #if did not find "na", it return -1
print(find_na)