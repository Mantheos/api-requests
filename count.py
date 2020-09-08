import pprint
import json
import requests



def count_profiles(token, filters):
    filters = filters

    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

    endpoint = "https://api.mantheos.com/profiles/count/"
    
    response = requests.post(endpoint, headers=headers, json=filters)
    
    request = json.loads(response.content)
    
    stats = request['request_stats']
    info = request['info']
    
    print('Info')
    pprint.pprint(info)
    print('\n')
    
    for stat in stats:
        print(stat)
        pprint.pprint(stats[stat])
        print('\n')

    return stats, info

