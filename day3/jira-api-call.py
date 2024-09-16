import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

dotenv_path = '/home/mdsk2001/devops/devops_python/day3/.env/jira_token.env'

# Load the .env file
load_dotenv(dotenv_path)
api_token = os.getenv("JIRA_API_TOKEN")

if api_token is None:
    raise ValueError("The JIRA_API_TOKEN environment variable is not set.")

url = "https://mdsk-2001.atlassian.net//rest/api/3/project"
auth = HTTPBasicAuth("mohammadsaubankhan@gmail.com", api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)

for name in output:
    print(name["name"])