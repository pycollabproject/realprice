import json

with open("algorithmstored") as stored_algorithm:
    stored_algorithm = json.load(stored_algorithm)
    print(stored_algorithm)
