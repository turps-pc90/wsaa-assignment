# Library Imports
import requests
import json
from config import api_keys as keys, usernames as acc
from github import Github, Auth

# Using access token as per README - https://github.com/PyGithub/PyGithub
auth = Auth.Token(keys["githubkey"])

# The aim of the script below is to access the andrews.txt file
# from the GitHub repo and change the content of the file. 

g = Github(auth=auth)


# Testing for successful connection
user = g.get_user()
print(f"Authenticated as: {user.login}")

# Find GitHub objects
for repo in g.get_user().get_repos():
    print(repo.name)
    
# Close connection
g.close()