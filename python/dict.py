#dict -> dictionary help us associate a value with another(key value pair)

fruit = {
        "red" : "apple",
        "blue" : "blue berries",
        "pink" : "guava"
        }

print(fruit["red"])
print(fruit["blue"])
print(fruit["pink"])

fruit2 = [
        {"color" : "red","fruit" : "apple"},
        {"color" : "yellow","fruit":"banana"},
        {"color" : "pink","fruit":"guava"}
        ]

for fruit2 in fruit2:
    print(fruit2["color"],fruit2["fruit"])