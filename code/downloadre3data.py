#Downloads the repositories from re3data APIs

import urllib.request
import xml.etree.ElementTree as ET

baseUrl = 'https://www.re3data.org/'

response = urllib.request.urlopen(baseUrl + "api/v1/repositories")
root = ET.fromstring(response.read())

repos = root.findall('.//repository')

for r in repos:
    id = r.find('./id').text
    link = r.find('./link')
    response = urllib.request.urlopen(baseUrl + link.attrib['href'])
    fout = open('../data/re3dataRecords/' + id + '.xml', 'w')
    r = fout.write(response.read().decode('utf-8'))
    fout.close()
