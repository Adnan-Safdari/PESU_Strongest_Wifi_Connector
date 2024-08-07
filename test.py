import json

with open("config/Credentials.json", "r") as file:
    data = json.load(file)

print(data['username'])