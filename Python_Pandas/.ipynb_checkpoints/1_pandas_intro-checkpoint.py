import pandas as pd

dict1 = {
    "Name": ['Shakib','Hridoy','Mohan','Robi'],
    "Marks": [20,25,12,34],
    "City": ['Alahabad','Amitnagar','Sujagaong','Dakkhingbag']
}
# print(dict1)
df = pd.DataFrame(dict1)

print(df)