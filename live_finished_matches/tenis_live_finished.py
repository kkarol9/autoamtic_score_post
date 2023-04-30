import json

with open ('tenis.json') as f:
    jsondata = json.load(f)


#tournament = jsondata['events'][0]['tournament']['name']
#print(tournament)

for match in jsondata['events']:

    tournament = match['tournament']['name']
    #round = match['roundInfo'].get('name', 'Runda nieznana')
    name_1 = match['homeTeam']['name']
    #country_1 = match['homeTeam']['country']['name']
    country_1 = match['homeTeam']['country'].get('name', 'Team')


    name_2 = match['awayTeam']['name']
    #country_2 = match['awayTeam']['country']['name']
    country_2 = match['awayTeam']['country'].get('name', 'Team')


    #score_1_set_1 = match['homeScore']['period1']
    score_1_set_1 = match['homeScore'].get('period1', '')
    #score_1_set_2 = match['homeScore']['period2']
    score_1_set_2 = match['homeScore'].get('period2', '')
    #score_1_set_3 = match['homeScore']['period3']
    score_1_set_3 = match['homeScore'].get('period3', '')


    #score_2_set_1 = match['awayScore']['period1']
    score_2_set_1 = match['awayScore'].get('period1', '')

    #score_2_set_2 = match['awayScore']['period2']
    score_2_set_2 = match['awayScore'].get('period2', '')
    #score_2_set_3 = match['awayScore']['period3']
    score_2_set_3 = match['awayScore'].get('period3', '')


    
    print(tournament, "|", name_1, country_1, " - ", name_2, country_2, score_1_set_1, ":", score_2_set_1,   
        score_1_set_2, ":", score_2_set_2, score_1_set_3, ":", score_2_set_3)