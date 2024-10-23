def main():
    val = input("Item: ")
    fruits = {
        "Apple": "130",
        "Avocado": "50",
        "Cantolupe": "50",
        "Honeydew Melon": "50",
        "Pineapple": "50",
        "Strawberries": "50",
        "Tangerine": "50",
        "Banana": "110",
        "Grapefruit": "60",
        "Nectarine": "60",
        "Peach": "60",
        "Grape": "90",
        "Kiwifruit": "90",
        "Lemon": "15",
        "Lime": "20",
        "Orange": "80",
        "Watermelon": "80",
        "Pear": "100",
        "Sweet Cherries": "100",
        "Plums": "70",
    }
    
    if val in fruits:
        print(f"Calories: {fruits[val]}")
    else:
        print("Item not found.")
    
main()
