class Jar:
    def __init__(self, capacity=12,size = 0):
        if capacity < 1 :
            raise ValueError
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity :
            final_cookies = self.capacity - self.size
            self.size += final_cookies
            print(f"Cant Deposit {n-final_cookies} 🍪(s)")
        else :
            self.size += n

    def withdraw(self, n):
        if n > self.size :
            print(f"Removed {self.size} 🍪(s)")
            self.size -= self.size
        else :
            print(f"Removed {n} 🍪(s)")
            self.size -= n

    @property
    def _capacity(self):
        return self.capcity

    @property
    def _size(self):
        return self.size
    
def main():
    jar = Jar(10, 5)
    
    jar.deposit(3)
    print(jar)
    
    jar.withdraw(4)
    print(jar)
    
    jar.deposit(12)
    print(jar)
    
    jar.withdraw(100)
    print(jar)

if __name__ == "__main__":
    main()