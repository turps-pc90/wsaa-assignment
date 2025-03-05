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

# Define repo and file path
repo_name = "turps-pc90/wsaa-assignment"
file_name = "AssignmentTextFiles/andrews.txt"
branch = "main"

# Testing for successful connection
#user = g.get_user()
#print(f"Authenticated as: {user.login}")

# Find GitHub objects
#for repo in g.get_user().get_repos():
#    print(repo.name)
    
# Find specific repository
solo_repo = g.get_repo(repo_name)

# List files - https://pygithub.readthedocs.io/en/stable/examples/Repository.html
# contents = solo_repo.get_contents("")
#for content_file in contents:
#    print(content_file)

# Read specific file in repo - https://github.com/PyGithub/PyGithub/issues/576
content = solo_repo.get_contents("AssignmentTextFiles/andrews.txt")

# Initially I got an error relating to not having SHA value. 
# I had missed the content.sha reference here - https://pygithub.readthedocs.io/en/latest/examples/Repository.html#update-a-file-in-the-repository
file_sha = content.sha

raw_data = content.decoded_content.decode("utf-8")
#print(raw_data)

# Update specific file in repo - https://pygithub.readthedocs.io/en/stable/examples/Repository.html#update-a-file-in-the-repository
# str.replace function - https://docs.python.org/3/library/stdtypes.html#str.replace
updated_data = raw_data.replace("Andrew", "Paul")

solo_repo.update_file(file_name,
                    "Updated andrews.txt: Replaced 'Andrew' with 'Paul'",
                    updated_data,
                    file_sha,
                    branch=branch)
    
print(f"Updated {file_name} successfully!")

# Close connection
g.close()