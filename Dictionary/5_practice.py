# list of divition having information of district, upozila and council

total_divisions = {
    "Barishal": {"District": 6, "Upozila": 39, "Council": 333},
    "Dhaka": {"District": 13, "Upozila": 93, "Council": 1833},
    "Sylhet": {"District": 4, "Upozila": 38, "Council": 334},
    "Rajshahi": {"District": 8, "Upozila": 70, "Council": 558}
}

print(total_divisions)
total_divisions["Sylhet"] = {"District": 4, "Upozila": 38, "Council": 334, "Union": 241}      # mutatoin in dictionary.

print(total_divisions["Sylhet"])

name_of_divisions = total_divisions.keys()
print("Name of the keys in Division dictionary: ", total_divisions.keys())        # output: dict_keys(['Barishal', 'Dhaka', 'Sylhet', 'Rajshahi'])

for name in name_of_divisions:
    print(name, "Divison")

print("\nDivision Information: -------")
for info in total_divisions:
    print("\nInformation of","'", info,"'","Divisoin: ")
    print(total_divisions[info])