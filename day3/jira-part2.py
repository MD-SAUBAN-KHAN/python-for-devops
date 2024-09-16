from flask import Flask
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__) #created a flask instance 


#adding decorator
@app.route('/mdsk', methods =['POST'])
def hello():
    
    #dotenv_path = '/home/mdsk2001/devops/devops_python/day3/.env/jira_token.env'

    # Load the .env file
    #load_dotenv(dotenv_path)
    #api_token = os.getenv("JIRA_API_TOKEN")

    #if api_token is None:
    #   raise ValueError("The JIRA_API_TOKEN environment variable is not set.")

    url = "https://mdsk-2001.atlassian.net//rest/api/3/issue"
   # auth = HTTPBasicAuth("mohammadsaubankhan@gmail.com", "INSERT API TOKEN HERE")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "MY FIRST JIRA TICKET",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                        }
                        ],
                        "type": "doc",
                        "version": 1
                        },
            "issuetype": {
                "id": "10003"
                },

            "project": {
                "key": "MDSK"
                },


            "summary": "1st JIRA Tkt Created Successfully",
            },
        "update": {}
        } )

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
