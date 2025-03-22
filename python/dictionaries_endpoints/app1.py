
from app1_response import response

"""
TASK1
Connect to this API endpoint https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo 
Extract all senior roles and manager roles into a different list.
At the end you should have 2 lists , one for senior roles and the other for manager roles.
"""

jobs = response["jobs"]

senior_roles = []
manager_roles = []
for job in jobs:
    if (job["jobTitle"]) and ("Senior" in job["jobTitle"]):
        senior_roles.append(job["jobTitle"])
    elif (job["jobTitle"]) and ("Manager" in job["jobTitle"]): # ("Senior" not in job["jobTitle"]) and ("Manager" in job["jobTitle"]) :
        manager_roles.append(job["jobTitle"])

print(senior_roles)
print(manager_roles)


"""job_titles = [ job["jobTitle"] for job in jobs ] # Extract values in "jobTitle" key
senior_roles = []
manager_roles = []
for title in job_titles:
    if "Senior" in title:
        senior_roles.append(title)
    else:
        manager_roles.append(title)
"""
