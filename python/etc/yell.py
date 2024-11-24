# def main():
#     yell(["this", "is","cs50"])
# def yell(words):
#     uppercased = []
#     for word in words :
#         uppercased.append(word.upper())
#     print(uppercased)
#     print(*uppercased) ## this is to unpack the list ** is used to unpack dictionaries
# if __name__ == "__main__":
#     main()

def main():
    yell("This", "is", "cs50")
    
def yell(*words): ## * to take all the three values
    """ uppercased = map(str.upper,words)
    print(*uppercased) ##map is used to apply a given function to an iterable(here words is an iterable so we use map to apply upper function on the each element of the words... rather than using for loop) """
    uppercased = [word.upper() for word in words] ##this is list comprehension way to the same thing as did above
    print(*uppercased)
    
if __name__ == "__main__" :
    main()