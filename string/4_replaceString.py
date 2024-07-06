country = "North Korea"
new_country = country.replace("North", "South")
print(country, new_country)
new_country2 = country.replace("th", "dic")
print(new_country2)

#replace method returns a new string, it does not manipulate the existing string.

text = "th is a test1, th is test2, th is test3"
new_text = text.replace("th", "this")
print(new_text,"-------",text)                                         