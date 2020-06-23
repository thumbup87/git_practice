import json

filename = "user's favorite number.json"

with open (filename) as f:
    x = json.load(f)

print(f"your favorite number is {x}")