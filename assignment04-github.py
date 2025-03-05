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
#for repo in g.get_user().get_repos():
#    print(repo.name)
    
# Find specific repository
solo_repo = g.get_repo("turps-pc90/wsaa-assignment")

# List files - https://pygithub.readthedocs.io/en/stable/examples/Repository.html
# contents = solo_repo.get_contents("")
#for content_file in contents:
#    print(content_file)

# Read specific file in repo - https://github.com/PyGithub/PyGithub/issues/576
content = solo_repo.get_contents("AssignmentTextFiles/andrews.txt")
raw_data = content.decoded_content
print(raw_data)

# Update specific file in repo - https://pygithub.readthedocs.io/en/stable/examples/Repository.html#update-a-file-in-the-repository
content = solo_repo.get_contents("AssignmentTextFiles/andrews.txt")
print(content)
    
# Close connection
g.close()