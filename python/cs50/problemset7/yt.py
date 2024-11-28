import re
import sys

def main() :
    print(parse(input("HTML: ")))
    
def parse(str) :
    link = re.search(r'https://(?:www\.)youtube.com/embed/\w+',str)
    if link is not None :
        return link.group(0)
    else :
        return None
    
if __name__ == "__main__" :
    main()
