import pprint
import json
import requests



def get_history(token, page, page_size):

    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

    endpoint = f"https://api.mantheos.com/profiles/history/?page={page}&page_size={page_size}"
    
    response = requests.get(endpoint, headers=headers)
    
    history = json.loads(response.content)
    pprint.pprint(history)
    return history
