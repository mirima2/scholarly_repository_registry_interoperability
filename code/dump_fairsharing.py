import config
import requests
import json
import time

DATE = time.strftime('%Y-%m-%d')

url = "https://api.fairsharing.org/users/sign_in"

payload="{\"user\": {\"login\":\"%s\",\"password\":\"%s\"} }" % (config.fairsharing_username, config.fairsharing_password)
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
token = response.json()['jwt']
# print(jwt)

# Get the JWT from the response.text to use in the next part.

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + token,
}
# print(headers)

with open('../data/fairsharing_dump_%s.json' % DATE, 'w') as file_out:
    page = 1
    size = 500
    while(True):
        url = 'https://api.fairsharing.org/databases/?page[number]=%s&page[size]=%s' % (page,size)
        print(url)

        response = requests.request("GET", url, headers=headers)
        file_out.writelines('\n'.join([json.dumps(record) for record in response.json()['data']]))
        file_out.write('\n')

        if len(response.json()['data']) < size:
            break
        page += 1