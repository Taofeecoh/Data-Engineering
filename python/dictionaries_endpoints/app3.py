import requests

"""
TASK3
Connect to this API endpoint https://randomuser.me/api/?results=500
Extract all male and female profiles into a different list
At the end you should have 2 lists , one for male and the other for female.

Extract all dob date into a list.
You will see the dob key with a value containing 2 keys date and age. We are only interested in the date.

Extract that date into a list
Extract concatenated first name and last name into a list

This means you will find a way to extract the first name, last name and concatenate them together to make a full name, make sure you send the full name into a list.
"""


url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
user_data = response.json()

male_profile = []
female_profile = []
date_list = []
names_list = []

for user in user_data["results"]:
    if user["gender"] == "male":
        male_profile.append(user)
    elif user["gender"] == "female":
        female_profile.append(user)

    if user["dob"]:
        date_list.append(user["dob"]["date"])
    
    if user["name"]:
        full_name = f"{user["name"]["first"]} {user["name"]["last"]}"
        names_list.append(full_name)

print(male_profile)
print(female_profile)
print(date_list)
print(names_list)