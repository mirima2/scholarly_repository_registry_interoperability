import pandas as pd

csv = pd.read_csv('../data/export_roar_CSV_20230131.csv')

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
for value in csv.values:
    if pd.isna(value[1]):
        continue
    count += 1
    #Generality
    if not pd.isna(value[0]):
        coverage['identifier'] += 1
    if not(pd.isna(value[31])):
        coverage['name'] += 1
    if not pd.isna(value[30]):
        coverage['repositoryURL'] +=1
    if not pd.isna(value[10]):
        coverage['repositoryType'] += 1
    if not pd.isna(value[36]):
        coverage['repositoryDescription'] += 1
    if not pd.isna(value[56]):
        coverage['recordCount'] += 1
    #Organization
    if not(pd.isna(value[40])):
        coverage['organizationName'] += 1
    if not pd.isna(value[42]):
        coverage['organizationCountry'] +=1
    if not pd.isna(value[44]):
        coverage['organizationLocationLat'] += 1
    if not pd.isna(value[45]):
        coverage['organizationLocationLong'] += 1
    if not pd.isna(value[41]):
        coverage['organizationUrl'] += 1
    #Content classification
    if not pd.isna(value[49]):
        coverage['subject'] += 1
    #Technical Info
    if not pd.isna(value[46]):
        coverage['softwareName'] += 1
    if not pd.isna(value[48]):
        coverage['softwareVersion'] += 1
    if not pd.isna(value[32]):
        coverage['apiUrl'] += 1
    #Dates and times
    if not pd.isna(value[50]):
        coverage['startDate'] += 1
    if not pd.isna(value[8]):
        coverage['lastUpdate'] += 1
    #Legal aspects

print(coverage)
print(count)