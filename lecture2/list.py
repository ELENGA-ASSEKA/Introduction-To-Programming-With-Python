#Get the students list
students = ["Hermione", "Harry", "Ron", "Draco"]


print(students[0])
print(students[1])
print(students[2])
print()
print()

#Get further for the good understanding
#students = ["Hermoine", "Harry", "Rion"]
for student in students:
    print(student)
print()
print()
#Let go further on using the len
for i in range(len(students)):
    print(i + 1, students[i])
print()
print()
print()

#Use Dictionary
students = {"Hermione": "Gryffindor",
         "Herry": "Gryffindor",
         "Ron": "Gryffindor",
         "Draco": "Slytherin"
        }
print(students["Hermione"])
print(students["Herry"])
print(students["Ron"])
print(students["Draco"])
print()
print()

#To go further
for student in students:
    print(student)
print()
print()

#Use this if you want to print the students names and houses
for student in students:
    print(student, students[student], sep=", ") 