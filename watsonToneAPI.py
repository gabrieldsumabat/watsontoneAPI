import json
import requests
from watson_developer_cloud import ToneAnalyzerV3

def watsonAPI(text):
    tone_analyzer = ToneAnalyzerV3(
       username='1fe1f790-1438-49c3-b0a6-816d9b91121d',
       password='jpy4qzzKlfV0',
       version='2016-05-19 ')
    dumpReturned=json.dumps(tone_analyzer.tone(text=text), indent=2)
    data=json.loads(dumpReturned)  
    toneValues=[]
    section=0
    for i in data['document_tone']['tone_categories']:
        toneValues.append([i['category_name']])
        for j in i['tones']:
           #print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))  
           toneValues[section].append(int(round(j['score']*100)))
        section+=1
    return toneValues

if __name__=="__main__":
    ##Auth
    tone_analyzer = ToneAnalyzerV3(
       username='1fe1f790-1438-49c3-b0a6-816d9b91121d',
       password='jpy4qzzKlfV0',
       version='2016-05-19 ')
    ##Run API Analysis to Return Values
    dumpReturned=json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2)
    data=json.loads(dumpReturned)  ##Type:DICT
    ##Display the returned data in a matrix
    toneValues=[]
    section=0
    for i in data['document_tone']['tone_categories']:
    ##    print(i['category_name'])
    ##    print("-" * len(i['category_name']))
        toneValues.append([i['category_name']])
        for j in i['tones']:
           print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
           toneValues[section].append(int(round(j['score']*100)))
        section+=1
    print(toneValues)

