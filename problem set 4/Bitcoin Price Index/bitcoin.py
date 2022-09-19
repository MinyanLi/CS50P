import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

if n < 0:
    sys.exit("Command-line argument is not a positive number")


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

ori = response.json()
bpi = ori["bpi"]
usd = bpi["USD"]
rate = usd["rate_float"]

print(f"${(n * rate):,.4f}")

