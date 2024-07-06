marks = [23,32,54,15,2,432,3]
roll = int(input("please enter your roll number: "))
print("your marks: ",marks[roll-1])

# store the marks of Bengali and Math subject of 5 student 

marks2 = [[20,40],[23,40],[21,22],[12,40],[30,12]]     # here we stored each student bengali and math marks in one list and all the marks stored inside of one big list
#[[begnali,math], [bengali, math]...]

#give me the marks of bengali and math of the 3rd student?
print(marks2[2])
#give me the marks of bengali subject of the 3rd student?
print(marks2[2][0])
#give me the marks of math subject of the 3rd student?
print(marks2[2][1])



# -------------------

# everything here is messy code.

# here the jem: Dictionary Data Structure

marks = {1:77, 11:80, 22:55, 4: 92, 2: "Fail" }     # DICTIONARY.
# give me the marks of roll number: 4 student?
print("marks of roll: 4 is - ", marks[4])
# give me the marks of roll number: 2 student?
print("marks of roll: 2 is - ", marks[2])
# give me the marks of roll number: 1 student?
print("marks of roll: 1 is - ", marks[1])
# give me the marks of roll number: 22 student?
print("marks of roll: 22 is - ", marks[22])