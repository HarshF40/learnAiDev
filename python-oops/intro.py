##classes in python

class Student:
  ##method instances (default constructor)
  ##self is like this operator from c++
  ##first arg is this ptr
  def __init__(self,name,house):
    self.name = name
    self.house = house ##this will call the settter automatically
    
  ##this function is automaticcally called when and object of class student is passed to a print function... this basically converts the objects into the string
  def __str__(self):
    return f"Name :{self.name} from House: {self.house}"
  
  
  ##for the getter and setter we give the same name as variable... so that interpreter understands it... and we give a different name to the variable inside it so that it doesnt go in infinite recursion... 
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self,name):
    if not name :
      raise ValueError("Missing Name")
    self._name = name
  
  ##getters(@property) and setters(method.setter)
  @property  ##to create a getter
  def house(self):
    return self._house ## _ to avoid infinite recursion
  
  @house.setter ##to create a setter... all the statements which will include .house = will automatically call this funtion.... 
  def house(self,house):
    print("Setter Called")
    self._house = house ## _ to avoid infinite recursion
    
##this function creates a student object and returns it...
  @classmethod
  def get(cls):
    name = input("Name: ")
    house = input("House: ")
    return cls(name,house)

def main():
  student = Student.get()
  print(student)
  student.house = "Egg Head" ##this will call the setter automatically ## but if we change house to _house we can access do the thing which the setter is doing... and no calls to the setter will be made it will be directly change the value
  
if __name__ == "__main__":
  main()
  
  ##to create an object of a class we can do var = Class() ## this will create an=empty object