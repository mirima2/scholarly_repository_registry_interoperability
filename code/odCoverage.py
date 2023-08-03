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

#'system_metadata.id\t
# repository_metadata.name\t
# repository_metadata.alternativename\t
# repository_metadata.url\t
# repository_metadata.description\t
# repository_metadata.type\t
# repository_metadata.content_languages\t
# system_metadata.date_modified\t
# system_metadata.date_created\t
# repository_metadata.content_subjects\t
# repository_metadata.content_types\t
# organization\t
# policy_urls\t
# repository_metadata.software\t
# repository_metadata.oai_url\t
# system_metadata.publicly_visible\t
# repository_metadata.repository_status\t
# repository_metadata.fulltext_record_count\t
# repository_metadata.metadata_record_count\n'
#{"repository_metadata": {"content_types": ["journal_articles", "bibliographic_references", "theses_and_dissertations", "unpub_reports_and_working_papers", "books_chapters_and_sections", "learning_objects"], "type": "institutional", "name": [{"name": "Alexandria Research Platform", "language": "en", "preferred_phrases": [{"phrase": "Name", "language": "en", "value": "name"}], "preferred": "name", "language_phrases": [{"value": "en", "language": "en", "phrase": "English"}]}], "metadata_record_count": 43608, "software": {"name_phrases": [{"value": "eprints", "language": "en", "phrase": "EPrints"}], "name": "eprints"}, "content_subjects": ["arts", "engineering", "health_and_medicine", "humanities", "mathematics", "science", "social_sciences", "technology"], "content_types_phrases": [{"phrase": "Journal Articles", "language": "en", "value": "journal_articles"}, {"phrase": "Bibliographic References", "language": "en", "value": "bibliographic_references"}, {"value": "theses_and_dissertations", "language": "en", "phrase": "Theses and Dissertations"}, {"language": "en", "value": "unpub_reports_and_working_papers", "phrase": "Reports and Working Papers"}, {"language": "en", "value": "books_chapters_and_sections", "phrase": "Books, Chapters and Sections"}, {"language": "en", "value": "learning_objects", "phrase": "Learning Objects"}], "full_text_record_count": 0, "url": "http://www.alexandria.unisg.ch/", "oai_url": "https://www.alexandria.unisg.ch/cgi/oai2", "content_subjects_phrases": [{"value": "arts", "language": "en", "phrase": "Arts"}, {"language": "en", "value": "engineering", "phrase": "Engineering"}, {"language": "en", "value": "health_and_medicine", "phrase": "Health and Medicine"}, {"value": "humanities", "language": "en", "phrase": "Humanities"}, {"phrase": "Mathematics", "language": "en", "value": "mathematics"}, {"language": "en", "value": "science", "phrase": "Science"}, {"phrase": "Social Sciences", "value": "social_sciences", "language": "en"}, {"phrase": "Technology", "value": "technology", "language": "en"}], "type_phrases": [{"phrase": "Institutional", "value": "institutional", "language": "en"}]}, "organisation": {"country": "ch", "identifiers": [{"type": "ror", "identifier": "https://ror.org/0561a3s31", "type_phrases": [{"phrase": "ROR ID", "language": "en", "value": "ror"}]}], "country_phrases": [{"language": "en", "value": "ch", "phrase": "Switzerland"}], "url": "https://www.unisg.ch", "name": [{"preferred": "name", "language_phrases": [{"value": "en", "language": "en", "phrase": "English"}], "language": "en", "preferred_phrases": [{"value": "name", "language": "en", "phrase": "Name"}], "name": "University of St. Gallen"}]}, "system_metadata": {"date_modified": "2022-07-11 15:50:30", "id": 2, "date_created": "2006-04-04 12:43:18", "publicly_visible_phrases": [{"phrase": "Yes", "language": "en", "value": "yes"}], "publicly_visible": "yes", "uri": "https://v2.sherpa.ac.uk/id/repository/2"}}
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