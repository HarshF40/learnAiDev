def convert(str):
    word = str.split()
    for i in range(len(word)):
        if word[i] == ":)":
            word[i] = "🙂"
        elif word[i] == ":(":
            word[i] = "🙁"
    return " ".join(word) #this joins the seperated word with the seperator

def main():
    strg = input("Input: ")
    print(convert(strg))

main()