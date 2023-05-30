import json

with open('tenis.json') as f:
    jsondata = json.load(f)

tab = []

for match in jsondata['events']:
    status = match['status']['type']
    match_id = match['customId']
    if status == 'finished':
        tab.append(match_id)

i = 0
print(tab)
for match in jsondata['events']:
    status = match['status']['type']
    match_id = match['customId']

    if status == 'finished' and match_id not in tab:

        print(status, match_id, i)
        i+=1