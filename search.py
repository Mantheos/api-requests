import pprint
import json
import time
import requests
import math


def profile_search(token, filters):
    # post request
    filters = filters
    
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    endpoint = "https://api.mantheos.com/profiles/"
    
    response = requests.post(endpoint, headers=headers, json=filters)
    response_content = json.loads(response.content)
    
    if 'request' in response_content:
        request = json.loads(response.content)['request']
    else:
        return response_content

    job_id = request['id']
    
    print('Getting Profiles')
    
    if request['requestDataIn'] != None:
        processing_time = math.ceil(float(request['requestDataIn']))
        print('Estimated wait time: ' + str(processing_time) + 's')
        while processing_time:
            mins, secs = divmod(processing_time, 60)
            timer = f'{mins:02d}:{secs:02d}'
            print(timer, end='\r')
            time.sleep(1)
            processing_time -= 1

    # get request
    endpoint = f"https://api.mantheos.com/profiles/?id={job_id}"
    
    # checks the status of the order
    response = requests.get(endpoint, headers=headers)
    results = json.loads(response.content)['results']
    status = results['status']
    
    tries = 0
    while 20 <= status < 29: 
        response = requests.get(endpoint, headers=headers)
        results = json.loads(response.content)['results']
        status = results['status']
        print("Checking the status of your order. Status: "+ str(status) + " Retries: " + str(tries), end='\r')
        time.sleep(2)
        tries += 1

    profiles = results['profiles']
    
    print('Profiles Ready')
    
    pprint.pprint(profiles)
    
    return profiles