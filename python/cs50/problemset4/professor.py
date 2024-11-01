import random

def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score: {score}/10")
    
def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if 0 < lvl < 4 :
                return lvl
            else :
                continue
        except ValueError :
            pass
        
def generate_integer(level):
    count = 0
    score = 0
    while count < 10 :
        if level == 1 :
            x = random.randint(0,9)
            y = random.randint(0,9)
        if level == 2 :
            x = random.randint(10,99)
            y = random.randint(10,99)
        if level == 3 :
            x = random.randint(100,999)
            y = random.randint(100,999)
        chance = 0
        while True :
            try:
                if chance == 3 :
                    print(f"{x} + {y} = {x+y}")
                    break
                _input = int(input(f"{x} + {y} = "))
                if _input == x + y :
                    score+=1
                    break
                else :
                    print("EEE")
                    chance+=1
            except ValueError :
                    print("EEE")
                    chance+=1
        count+=1
    return score
        
if __name__ == "__main__" :
    main()