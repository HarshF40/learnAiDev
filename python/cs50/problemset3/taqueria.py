menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def taqueria():
    total = 0
    while True:
        try:
            item = input("Input: ")
        except:
            pass
        else:
             total += menu[item.title()] #converts item to title cased
             print(f"Total: ${total}")
            
def main():
    taqueria()
    
main()