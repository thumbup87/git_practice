import json

filename = "my favorite number.json"

#checking whether filename is already stored.
try:
    with open (filename) as f:
        x = json.load(f)

#if not stored, execute the following        
except FileNotFoundError:
    print("your answer is not yet stored")
    #prompt the user for answer
    user_input = input("what is your favorite number? ")
    #create a filename and dump user's input
    with open (filename, 'w') as f:
        json.dump(user_input, f)
    #load information to memory 
    with open (filename) as f:
        x = json.load(f)

#When try succeeds else is executed.
#and it will be loaded to memory. And printed out.
else:
    with open (filename) as f:
        x = json.load(f)

#Either from except or else variable x is passed.
print(f"your favorite number is {x}")