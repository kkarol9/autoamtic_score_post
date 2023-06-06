import json
from PIL import Image, ImageDraw, ImageFont
import os


with open('tenis.json') as f:
    jsondata = json.load(f)

with open('match_id2.json') as f:
    match_id_lista = json.load(f)

zawodnicy = {}
i = 0

for match in jsondata['events']:
    status = match['status']['type']
    match_id = match['customId']
    if status == 'finished' and match_id not in match_id_lista:
        print("jestem")
        tournament = match['tournament']['name']
        name_1 = match['homeTeam']['name']
        name_2 = match['awayTeam']['name']
        #home_score1 = match['homeScore']['period1']
        home_score1 = match['homeScore'].get('period1')
        #home_score2 = match['homeScore']['period2']
        away_score1 = match['awayScore'].get('period1')
        #away_score2 = match['awayScore']['period2']
        name_1 = name_1.encode('utf-8')
        name_2 = name_2.encode('utf-8')
        tournament = tournament.encode('utf-8')

        print(home_score1, away_score1)




        zawodnicy = {
            'tournament': tournament,
            'name1': name_1,
            'name2': name_2
        }
        match_id_lista.append(match_id)


with open('match_id2.json', 'w') as f:
    json.dump(match_id_lista, f)

