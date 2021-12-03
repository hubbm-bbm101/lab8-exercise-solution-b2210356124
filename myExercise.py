import sys
studentsdict={}
with open (sys.argv[1]) as StudentFile:
    for line in StudentFile:
        attempt = line.split(":")
        studentsdict[attempt[0]] = attempt[1]
names=sys.argv[2]
namesList=[]
if names.count(",") == 0:
    namesList.append(names)
else:
    namesList=names.split(",")
for i in namesList:
    if i in studentsdict :
        print(f"Name: {i}, University: {studentsdict[i]}")
    else:
        print(f"No record of '{i}' was found!")