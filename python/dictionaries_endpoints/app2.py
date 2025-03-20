import requests



"""
TASK2
Connect to this API endpoint http://api.football-data.org/v4/competitions/ 
Extract all the competition names into a separate list.
"""


url = "http://api.football-data.org/v4/competitions/"

response = requests.get(url)
competition_data = response.json()
competition_names = [comp["name"] for comp in competition_data["competitions"]]

print(competition_names)