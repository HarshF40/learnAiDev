##classes in python

class Student:
  ##method instances (default constructor)
  ##self is like this operator from c++
  ##first arg is this ptr
  def __init__(self,name,house):
    self.name = name
    self.house = house
    
def get_student():
  name = input("Name: ")
  house = input("House: ")
  return Student(name,house)

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")
  
if __name__ == "__main__":
  main()