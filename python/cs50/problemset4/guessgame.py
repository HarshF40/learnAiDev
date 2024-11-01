from random import randint

def main():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl < 0 :
                continue
            else:
                break
        except ValueError :
            pass
        
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0 :
                continue
            else :
                break
        except ValueError:
            pass
        
    num = randint(1,lvl)
    if guess > num :
        print("Too Large!")
    elif guess < num :
        print("Too small")
    elif guess == num :
        print("Just Right!")
            
main()