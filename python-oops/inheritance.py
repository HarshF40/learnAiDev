class Wizard:
    def __init__(self,name):
        if not name :
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard): ##Student is subclass of Wizard
    def __init__(self,name,house):
        super.__init__(name) ##super points to the super class
        self.house = house
        
class Professor:
    def __init__(self,name,subject): ##Professor is subclass of Wizard
        super.__init__(name) ##super points to th esuper class
        self.subject = subject