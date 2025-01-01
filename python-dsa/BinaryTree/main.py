class User:
    def __init__(self,username,name,email): #constructor method, self is always passed as the first arguement
        self.username = username
        self.name = name
        self.email = email
        #print("User Created")

    def introduce(self):
        print("Hi I am {}, My name is {}. Contact me on {}!".format(self.username, self.name, self.email))

    def __repr__(self): #this is used to format the __str__ call
        return "{}\n".format(self.name)

    def __str__(self): #this is invoked when we try to print the object directly with print. [print(user_obj)]
        return self.__repr__()

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        low = 0;
        high = len(self.users) - 1
        while low <= high :
            mid = (low+high) // 2
            if self.users[mid].username >= user.username >= self.users[mid-1].username :
                self.users.insert(mid,user)
            if self.users[mid].username < user.username :
                low = mid + 1
            else :
                high = mid - 1
#        i = 0
#        while i < len(self.users):
#            if self.users[i].username > user.username:
#                self.users.insert(i,user)
#                return
#            i+=1
#        self.users.append(user)

    def find(self, username):
       low = 0
       high = len(self.users) - 1
       while low <= high :
           mid = (low + high) // 2
           #print(mid, low, high)

           if username == self.users[mid].username :
               print(f"Found: {self.users[mid].username}")
               return self.users[mid]

           if username > self.users[mid].username :
               low = mid + 1
           else :
                high = mid - 1

       print("User Not Found")
       return User('','','');

    def update(self, user):
        if user.username == '' :
            return -1
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        print(self.users)

def main():

    #creating Users
    harsh = User('harshF40','Harsh Gaonker','dummy@gmale.tom')
    aakash = User('aakash', 'Aakash Rai', 'aakash@exmaple.com')
    biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
    hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')

    #creating list of all the users
    base = UserDatabase() #creating object of the UserDatabase which is a list of the users
    base.users = [aakash, biraj, harsh, hemanth, jadhesh]
    base.insert(User('damodardevil', 'Damodar Naik', 'damodar@devil.com'))
    base.insert(User("imu","Iman Jasoos","imu@sama.one"))
    base.list_all()
    base.find(aakash.username)
    if base.update(User('biraj', 'Birju Svolakiv Makarov', 'biraj@bimal.kes')) == -1 :
        print("User Not Found")
    print(biraj.name)
    if base.update(User('niraj', 'Birju Svolakiv Makarov', 'biraj@bimal.kes')) == -1 :
        print("User Not Found")

if __name__ == "__main__":
    main()
