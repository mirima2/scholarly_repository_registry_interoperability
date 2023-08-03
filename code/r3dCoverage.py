import glob
import xml.etree.ElementTree as ET

repo_list = glob.glob('../data/re3dataRecords/*.xml')

r3_coverage = {'identifier':0, 
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

dbRestricted = 0
dataRestrictied = 0

for repo in repo_list:
    root = ET.parse(repo).getroot()
    id = root.find('.//{http://www.re3data.org/schema/2-2}re3data.orgIdentifier')
    if not id is None and id.text != '':
        r3_coverage ['identifier'] += 1
    name =  root.find('.//{http://www.re3data.org/schema/2-2}repositoryName')
    if not name is None :
        if name.text != '':
            r3_coverage['name'] += 1
        if 'language' in name.attrib and name.attrib['language']!= '':
            r3_coverage['nameLanguage']  += 1 
    additionalname = root.find('.//{http://www.re3data.org/schema/2-2}additionalName')
    if not additionalname is None:
        if additionalname.text != '':
            r3_coverage['additionalName'] += 1
        if 'language' in additionalname.attrib and additionalname.attrib['language'] != '':
            r3_coverage['additionalNameLanguage'] += 1
    repoUrl = root.find('.//{http://www.re3data.org/schema/2-2}repositoryURL')
    if not repoUrl is None and repoUrl.text != '':
        r3_coverage['repositoryURL'] += 1
    type = root.find('.//{http://www.re3data.org/schema/2-2}type')
    if not type is None and type.text != '':
        r3_coverage['repositoryType']  += 1
    dex =  root.find('.//{http://www.re3data.org/schema/2-2}description')
    if not dex is None and dex.text != '':
        r3_coverage['repositoryDescription'] += 1
    ctype = root.find('.//{http://www.re3data.org/schema/2-2}contentType')
    if not ctype is None and ctype.text != '':
        r3_coverage['repositoryContent']  += 1
    repoId =  root.find('.//{http://www.re3data.org/schema/2-2}repositoryIdentifier')
    if not repoId is None and repoId.text != '':
        r3_coverage['recordURI'] += 1
    subjs = root.findall('.//{http://www.re3data.org/schema/2-2}subject')
    if len(subjs) > 0:
        for s in subjs:
            if s.text != '':
                r3_coverage['subject'] += 1
                break
    kws = root.findall('.//{http://www.re3data.org/schema/2-2}keyword')
    if len(kws) > 0:
        for k in kws:
            if k.text != '':
                r3_coverage['keyword'] += 1
                break
    ists = root.findall('.//{http://www.re3data.org/schema/2-2}institution')
    if len(ists) > 0:
        name = 0
        namel = 0
        addname = 0
        addnamel = 0
        country = 0
        url = 0
        ide = 0
        for i in ists:
            iname = i.find('.//{http://www.re3data.org/schema/2-2}institutionName') 
            if iname is not None:
                if iname.text != '':
                    name += 1
                    if 'language' in iname.attrib and iname.attrib['language'] != '':
                        namel += 1
            aname = i.find('.//{http://www.re3data.org/schema/2-2}institutionAdditionalName') 
            if aname is not None:
                if aname.text != '':
                    addname += 1
                    if 'language' in aname.attrib and aname.attrib['language'] != '':
                        addnamel += 1
            if i.find('.//{http://www.re3data.org/schema/2-2}institutionCountry') is not None and  i.find('.//{http://www.re3data.org/schema/2-2}institutionCountry').text != '':
                country += 1
            if i.find('.//{http://www.re3data.org/schema/2-2}institutionURL') is not None and i.find('.//{http://www.re3data.org/schema/2-2}institutionURL').text != '':
                url += 1
            if i.find('.//{http://www.re3data.org/schema/2-2}institutionIdentifier') is not None and i.find('.//{http://www.re3data.org/schema/2-2}institutionIdentifier').text != '':
                ide += 1
        if name > 0:
            r3_coverage['organizationName'] += 1
        if addname > 0:
            r3_coverage['organizationAcronym'] += 1
        if namel > 0 :
            r3_coverage['organizationNameLanguage'] += 1
        if country > 0:
            r3_coverage['organizationCountry'] += 1
        if url > 0:
            r3_coverage['organizationUrl'] += 1
        if ide > 0:
            r3_coverage['organizationId'] += 1
    software = root.findall('.//{http://www.re3data.org/schema/2-2}software')
    if len(software) > 0:
        for s in software:
            if s.find('.//{http://www.re3data.org/schema/2-2}softwareName') is not None and s.find('.//{http://www.re3data.org/schema/2-2}softwareName').text != '':
                r3_coverage['softwareName'] += 1
                break
    versioning = root.find('.//{http://www.re3data.org/schema/2-2}versioning')
    if versioning is not None and versioning.text != '':
        r3_coverage['versioning'] += 1
    api = root.findall('.//{http://www.re3data.org/schema/2-2}api')
    if len(api) > 0:
        url = 0
        type = 0
        for a in api:
            if a.text != '':
                url += 1
                if 'apiType' in a.attrib and a.attrib['apiType'] != '':
                    type += 1
        if type > 0:
            r3_coverage['apiType'] += 1
        if url > 0:
            r3_coverage['apiUrl'] += 1
    startDate = root.find('.//{http://www.re3data.org/schema/2-2}startDate')
    if not startDate is None and startDate.text != '':
        r3_coverage['startDate'] += 1
    lastUpdate = root.find('.//{http://www.re3data.org/schema/2-2}lastUpdate')
    if not lastUpdate is None and lastUpdate.text != '':
        r3_coverage['lastUpdate'] += 1
    #questo vale perche' se esiste il campo policy allora sono mandatory sia policyName che policyUrl
    policy = root.findall('.//{http://www.re3data.org/schema/2-2}policy')
    r3_coverage['policyName'] += len(policy)
    r3_coverage['policyUrl'] += len(policy)
    dbAccess = root.find('.//{http://www.re3data.org/schema/2-2}databaseAccess')
    if dbAccess is not None :
        r3_coverage['databaseAccessType'] += 1
        if dbAccess.find('.//{http://www.re3data.org/schema/2-2}databaseAccessType').text =='restricted':
            dbRestricted += 1
        if dbAccess.find('.//{http://www.re3data.org/schema/2-2}databaseAccessRestriction') is not None :
            r3_coverage['databaseAccessRestriction'] += 1
    dataUpload = root.find('.//{http://www.re3data.org/schema/2-2}dataUpload')
    if dataUpload is not None:
        r3_coverage['dataUploadType'] += 1
        if dataUpload.find('.//{http://www.re3data.org/schema/2-2}dataUploadType').text == 'restricted':
            dataRestrictied += 1
        if dataUpload.find('.//{http://www.re3data.org/schema/2-2}dataUploadRestriction') is not None :
            r3_coverage['dataUploadRestriction'] += 1
    dbLicense = root.findall('.//{http://www.re3data.org/schema/2-2}databaseLicense')
    if dbLicense is not None:
        r3_coverage['databaseLicenseName'] += 1
        r3_coverage['databaseLicenceUrl'] += 1
    dataLicence = root.findall('.//{http://www.re3data.org/schema/2-2}dataUploadLicense')
    if dataLicence is not None:
        r3_coverage['dataUploadLicenceName'] += 1
        r3_coverage['dataUploadLicenceUrl'] += 1



print(r3_coverage)
print(len(repo_list))
print(dataRestrictied)
print(dbRestricted)