import emoji

def main():
    string = input("input: ")
    first,_emoji,last = string.split(":")
    _emoji = emoji.emojize(":" + _emoji + ":",language = 'alias')
    string = first + _emoji + last
    print(string)

main()    