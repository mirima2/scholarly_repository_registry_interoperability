import json


od = open('../data/opendoar_dump_2023-02-01.json')
coverage = {'identifier':0, 
'name' : 0, 
'nameLanguage':0, 
'additionalName':0, 
'additionalNameLanguage':0, 
'repositoryURL':0, 
'repositoryType':0, 
'repositoryDescription':0, 
'repositoryContent':0, 
'recordURI':0, 
'recordCount':0, 
'subject':0,
'keyword':0,
'organizationId':0,
'organizationName':0,
'organizationAcronym':0,
'organizationNameLanguage':0,
'organizationCountry':0,
'organizationLocationLat':0,
'organizationLocationLong':0,
'organizationUrl':0,
'softwareName':0,
'softwareVersion':0,
'versioning':0,
'apiType':0,
'apiUrl':0,
'apiDocumentation':0,
'repository_status':0,
'startDate':0,
'lastUpdate':0,
'policyType':0,
'policyName':0,
'policyUrl':0,
'databaseAccessType':0,
'databaseAccessRestriction':0,
'dataUploadType' :0,
'dataUploadRestriction':0,
'databaseLicenseName':0,
'databaseLicenceUrl':0,
'dataUploadLicenceName':0,
'dataUploadLicenceUrl':0}


count = 0

for line in od:
    count += 1
    repo = json.loads(line)
    if repo['system_metadata']['id'] != '':
        coverage['identifier'] += 1
    if repo['system_metadata']['date_created'] != '':
        coverage['startDate'] += 1
    if repo['system_metadata']['date_modified'] != '':
        coverage['lastUpdate'] += 1
    dic = repo['repository_metadata']
   
    if 'name' in dic and dic['name'] != []:
        name_count = 0 
        name_lan = 0
        name_acr = 0
        for name in dic['name']:
            if 'name' in name and name['name'] != '':
                name_count +=1
            if 'language' in name and name['language'] != '':
                name_lan += 1
            if 'acronym' in name:
                name_acr += 1
        if name_lan > 1:
            coverage['nameLanguage'] += 1
        if name_acr > 1:
            coverage['additionalName'] += 1
        if name_count > 1:
            coverage['name'] += 1
    if 'url' in dic and dic['url'] != '':
        coverage['repositoryURL'] += 1
    if 'type' in dic and dic['type'] != '':
        coverage['repositoryType'] += 1
    if 'content_types' in dic and dic['content_types'] != []:
        coverage['repositoryContent'] += 1
    coverage['recordURI'] += 1
    if 'metadata_record_count' in dic and dic['metadata_record_count'] != '':
        coverage['recordCount'] += 1
    if 'content_subjects' in dic and dic['content_subjects'] != '':
        coverage['subject'] += 1
    if 'software' in dic and 'name' in dic['software'] and dic['software']['name'] != '':
        coverage['softwareName'] += 1
    if 'oai_url' in dic and dic['oai_url'] != '':
        coverage['apiUrl'] += 1
    if 'policy_urls' in dic:
        type = 0
        url = 0
        for p in dic['policy_urls']:
            if 'type' in p and p['type'] != '':
                type += 1
            if 'policy_url' in p and p['policy_url'] != '':
                url += 1
        if type > 0:
            coverage['policyType'] += 1
        if url > 0:
            coverage['policyUrl'] += 1
    dic = repo['organisation']
    if 'name' in dic and dic['name'] != []:
        o_lan = 0
        o_acr = 0
        o_count = 0
        for name in dic['name']:
            if 'name' in name and name['name'] != '':
                o_count +=1
            if 'language' in name and name['language'] != '':
                o_lan += 1
            if 'acronym' in name:
                o_acr += 1
        if o_count > 1:
            coverage['organizationName'] += 1
        if o_acr > 1:
            coverage['organizationAcronym'] += 1
        if o_lan > 1 :
            coverage['organizationNameLanguage'] += 1
    if 'country' in dic and dic['country'] != '':
        coverage['organizationCountry'] += 1
    if 'url' in dic and dic['url'] != '':
        coverage['organizationUrl'] += 1
    if 'identifiers' in dic and dic['identifiers'] != []:
        id_num = 0
        for id in dic['identifiers']:
            if id['identifier'] != '':
                id_num +=1
        if id_num > 1:
            coverage['organizationId'] += 1



print(coverage)
print(count)