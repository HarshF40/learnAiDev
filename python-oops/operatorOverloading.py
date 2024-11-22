class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self,other) : ##overlaoding add operator
        galleons = self.galleons + other.galleons
        sickles  = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons,sickles,knuts)
    
potter = Vault(100,200,49)
weasly = Vault(125,43,342)
print(potter)
print(weasly)

total = potter + weasly
print(total)