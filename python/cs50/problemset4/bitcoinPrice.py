import sys
import requests
import json

def main():
    
    try:
        val = float(sys.argv[1])
    except ValueError :
        sys.exit("Command-line arguement is not a number!")
    except IndexError:
        sys.exit("Missing command-line arguement")
        
    response = (requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")).json()
    oneBitcoin = float(response["bpi"]["USD"]["rate_float"])  
    print(f"${val*oneBitcoin:,.4f}")
        
main()