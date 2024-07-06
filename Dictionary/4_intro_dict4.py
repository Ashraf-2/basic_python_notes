marks = {
    1: {"Bangla":30,"English":22},
    2: {"Bangla":20,"English":25},
    3: {"Bangla":25,"English":18},
    4: {"Bangla":22,"English":28}
}
print(marks)
print("Mark of roll 2: ")
print("Mark of roll 2 in Bangla: ")
print("Mark of roll 2 in English: ")

# using loop to print out individuals marks:

for roll in marks:
    print("Marks of Roll-"+str(roll)+" : "+str(marks[roll]))
    print("Marks of Roll-"+str(roll)+" in Bangla - "+str(marks[roll]["Bangla"]))
    print("Marks of Roll-"+str(roll)+" in English - "+str(marks[roll]["English"]))

    