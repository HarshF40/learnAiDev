item = []

def get_item():
    while True:
        try:
            val = input("Item: ").title()
            item.append(val)
        except EOFError:
            print("\n")
            for i in range(len(item)):
                count = 0
                flag = True
                for j in range(len(item)):
                    if j<i and item[i] == item[j]:
                        flag = False
                        break
                    elif item[i] == item[j]:
                        count+=1
                if flag:
                    print(f"{count} {item[i]}")
            print("\n")

def main():
    get_item();
    for element in item:
        print(element)

main()