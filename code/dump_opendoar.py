import config
import requests
import json
import time

DATE = time.strftime('%Y-%m-%d')

with open('../data/opendoar_dump_%s.json' % DATE, 'w') as file_out:
    size = 100
    offset = 0
    while(True):
        url = 'https://v2.sherpa.ac.uk/cgi/retrieve/cgi/retrieve?item-type=repository&api-key=%s&format=Json&limit=%s&offset=%s' % (config.opendoar_apikey, size, offset)
        print(url)

        response = requests.request("GET", url)
        file_out.writelines('\n'.join([json.dumps(record) for record in response.json()['items']]))
        file_out.write('\n')

        if len(response.json()['items']) < size:
            break
        offset += size