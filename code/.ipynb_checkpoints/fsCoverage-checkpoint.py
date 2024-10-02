import json
fs = open('../data/fairsharing_20230131.json')
fs_coverage = {'identifier':0, 
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

fs_count = 0
for line in fs:
    fs_count += 1
    dic = json.loads(line)
    attribute = dic['attributes']
    metadata = attribute['metadata']
    if 'identifier' in metadata and metadata['identifier'] != "":
        fs_coverage['identifier'] += 1
    if 'name' in metadata and metadata['name'] != "":
        fs_coverage['name'] += 1
    if 'abbreviation' in metadata and metadata['abbreviation'] != "":
        fs_coverage['additionalName'] += 1
    if 'homepage' in metadata and metadata['homepage'] != "":
        fs_coverage['repositoryURL'] +=1
    if 'description' in metadata and metadata['description'] != '':
        fs_coverage['repositoryDescription'] += 1
    if 'doi' in metadata and metadata['doi'] != "":
        fs_coverage['recordURI'] += 1
    else:
        print(metadata['identifier'])
    if 'data_versioning' in metadata and metadata['data_versioning'] != '':
        fs_coverage['versioning'] += 1
    if 'status' in metadata and metadata['status'] != '':
        fs_coverage['repository_status'] += 1
    if 'year_creation' in metadata and metadata['year_creation'] != '':
        fs_coverage['startDate'] += 1
    if 'data_access_condition' in metadata and metadata['data_access_condition'] != {}:
        if 'type' in metadata['data_access_condition'] and metadata['data_access_condition']['type'] != '':
            fs_coverage['databaseAccessType'] += 1
        if 'url' in metadata['data_access_condition'] and metadata['data_access_condition']['url'] != '':
            fs_coverage['databaseAccessRestriction'] += 1
    if 'data_deposition_condition' in metadata and metadata['data_deposition_condition'] != {}:
        if 'type' in metadata['data_deposition_condition'] and metadata['data_deposition_condition']['type'] != '':
            fs_coverage['dataUploadType'] += 1
        if 'url' in metadata['data_deposition_condition'] and metadata['data_deposition_condition']['url'] != '':
            fs_coverage['dataUploadRestriction'] += 1
    if 'subjects' in attribute and attribute['subjects'] != []:
        fs_coverage['subject'] += 1
    if 'user_defined_tags' in attribute and attribute['user_defined_tags'] != []:
        fs_coverage['keyword'] += 1
    if 'grants' in attribute and attribute['grants'] != []:
        for g in attribute['grants']:
            if g['saved_state']['name'] != '':
                fs_coverage['organizationName'] += 1
                break
    if 'licence_links' in attribute and attribute['licence_links'] != []:
        for lic in attribute['licence_links']:
            if 'licence_name' in lic and lic['licence_name'] != '' and 'licence_url' in lic and lic['licence_url'] != '':
                fs_coverage['databaseLicenceUrl'] += 1
                fs_coverage['databaseLicenseName'] += 1
                break 


print(fs_coverage)
print (fs_count)