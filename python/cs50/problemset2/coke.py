def main():
    money = 50
    while money<=50 and money>0 : 
        change_owed = 0
        print(f"Amount Due: {money}")
        insertAmt = int(input("Insert Coin: "))
        if insertAmt == 10 or insertAmt == 25 or insertAmt == 5 :
            money-=insertAmt
            if money < 0 :
                change_owed = -1*money
                break
        else :
            continue

    if money<0 :
        print(f"Change Owed: {change_owed}")
            


if __name__ == "__main__":
    main()