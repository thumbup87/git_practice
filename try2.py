import json

filename = "user's favorite number.json"

user_input = input("what is your favorite number? ")

with open (filename, 'w') as f:
    json.dump(user_input, f)

