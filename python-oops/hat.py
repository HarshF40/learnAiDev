import random

class Hat:
    houses = ["House1","House2","House3","House4"] ##class varaibles are shared across all the instances and variables inside the init method are unique to each instance
     
    @classmethod  ##classmethod are methods that are bound to the class not an instance, so they operate on class
    def sort(cls,name):
        print(name, "is in", random.choice(cls.houses))
        
Hat.sort("Harry")