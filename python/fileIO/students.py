#we use .csv(comma seperated values) files rather than the normal .txt files to store multiple types of data related to one data, .csv files are widely used than the .txt files

# name = input("Name: ")
# house = input("House: ")
# with open("students.csv","a") as file :
#     file.write(name+","+house+"\n")

#to read the data in the files
# with open("students.csv","r") as file :
#     for line in sorted(file) :
#         row = line.rstrip().split(",") # or name , house = line.rstrip().split(",")
#         print(f"{row[0]} is in the house {row[1]}")

#we can sort in a better way
students = [] # empty list

with open("students.csv","r") as file :
    for line in file :
        name , house = line.rstrip().split(",")
        student = {"name" : name , "house" : house} # creates a dictionary
        students.append(student) #appending the dictionary to the list to create a list of the dictionary
        
#to sort the dictionary we have to provide a key value to the sorted function to sort on that key value as dictionaries have many values.... we can sort the dictionary on any value... so to provide a key value we define a getter to get that key... 
#in sorted by default key is set to NONE and reverse is set to False

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

#but its not always necessary to define a whole function, so we use lambda function, which has no name
#syntax of lambda function below, where lamda indicates that the function is a lambda function and student is the parameter and student["name"] is the value which will be returned by lambda function
#the below syntax is equivalent to 
# def get_name(student):
#     return student["name"]
        
for student in sorted(students, key = lambda student : student["name"], reverse = False) :
    print(f"{student['name']} is in {student['house']}")