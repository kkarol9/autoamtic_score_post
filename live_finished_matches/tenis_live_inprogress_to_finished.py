import json

with open ('tenis.json') as f:
    jsondata = json.load(f)


#tournament = jsondata['events'][0]['tournament']['name']
#print(tournament)
in_progress = []
in_progress_ids = []
finished = []

for match in jsondata['events']:

    match_id = match['id']
    status = match['status']['type']

    if match_id in in_progress_ids:
        if status == 'finished':
            tournament = match['tournament']['name']
            name_1 = match['homeTeam']['name']
            country_1 = match['homeTeam']['country'].get('name', 'Team')
            name_2 = match['awayTeam']['name']
            country_2 = match['awayTeam']['country'].get('name', 'Team')
            score_1_set_1 = match['homeScore'].get('period1', '')
            score_1_set_2 = match['homeScore'].get('period2', '')
            score_1_set_3 = match['homeScore'].get('period3', '')
            score_2_set_1 = match['awayScore'].get('period1', '')
            score_2_set_2 = match['awayScore'].get('period2', '')
            score_2_set_3 = match['awayScore'].get('period3', '')
            
            print(f"{tournament} | {name_1} {country_1} - {name_2} {country_2} {score_1_set_1}:{score_2_set_1} {score_1_set_2}:{score_2_set_2} {score_1_set_3}:{score_2_set_3} {status}")
                
            in_progress_ids.remove(match_id)
            in_progress.remove(match)
    elif status == 'inprogress':
        print("jestem")
        in_progress_ids.append(match_id)
        in_progress.append(match)


