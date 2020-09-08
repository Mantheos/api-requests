import pprint
import json
import requests



def linkedin_search(token, profile_url):
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

    endpoint = "https://api.mantheos.com/profiles/linkedin-url/"

    data = {
        "profileUrl": f"https://www.linkedin.com/in/{profile_url}",
    }

    response = requests.post(endpoint, headers=headers, json=data)
    response_content = json.loads(response.content)
    request = response_content['request']
    status = request['status']
    if status != 30:
        return "Status Code: "+  str(status)
    else:
        profile = request['profile']

        pprint.pprint(profile)
        return profile