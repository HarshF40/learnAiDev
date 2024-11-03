import csv

students = []

with open("csvStudents.csv","r") as file :
#   reader = csv.reader(file) #reads the file as per csv and handles all the corner cases
#we can access the csv file in a more better way using DictReader
  reader = csv.DictReader(file) #returns a dictionary based on the key values specified on the top of the .csv file
  for row in reader :
      students.append({"name" : row["name"] ,"home" : row["home"]})
        
for student in sorted(students, key = lambda student : student["name"], reverse = False):
    print(f"{student['name']} is from {student['home']}")