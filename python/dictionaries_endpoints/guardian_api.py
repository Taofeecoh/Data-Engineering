
"""
TASK
- Access the url link https://open-platform.theguardian.com/
- Read through the documentation
- Create a function to extract articles with keyword 'Nigeria' in the year 2025.
- Convert this into a dataframe
- Export into a CSV.
"""

import requests
import pandas as pd

url = "https://content.guardianapis.com/search?q=%22Nigeria%22&api-key=test"

r = requests.get(url)
print(r.status_code)
response = r.json()

data = response["response"]
print(data.keys())
data = data["results"]

df = pd.DataFrame(data = data)
print(df.head())

df.to_csv('guardian_Nigeria.csv', encoding='utf-8', index=False, header=True)

############################################

def guardian_api(link):
    r = requests.get(link)
    if r.status_code == 200:
        response = r.json()
        data = response["response"]
        #print(data.keys())
        data = data["results"]
        df = pd.DataFrame(data = data)
        df.to_csv('guardianNigeria.csv', encoding='utf-8', index=False, header=True)
        #return(df)
    else:
        return f"Invalid status code"
    

