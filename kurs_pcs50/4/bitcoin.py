import sys
import requests
import json

try:
    x = float(sys.argv[1])
except:
    sys.exit("Missing command-line argument")


r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

a = r.json()

answer = (a["bpi"]["USD"]["rate_float"] * int(x))

print(f"${answer:,.4f}")