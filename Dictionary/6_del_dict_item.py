total_divisions = {
    "Barishal": {"District": 6, "Upozila": 39, "Council": 333},
    "Dhaka": {"District": 13, "Upozila": 93, "Council": 1833},
    "Sylhet": {"District": 4, "Upozila": 38, "Council": 334},
    "Rajshahi": {"District": 8, "Upozila": 70, "Council": 558}
}
print(total_divisions)
del(total_divisions["Barishal"])
print(len(total_divisions))