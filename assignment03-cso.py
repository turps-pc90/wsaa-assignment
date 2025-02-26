# Library Imports
import requests
import json

# Defining URL
url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en'
data = requests.get(url).json()

# Print data to check request works as intended. 
#print(data)

# Print out data in more readable format using JSON library dumps() function.
# Formatting was not requested in assignmnent but prefered for readability.
json_str = json.dumps(data, indent=4)
print(json_str)