import json
from PIL import Image, ImageDraw, ImageFont
import os


with open('tenis.json') as f:
    jsondata = json.load(f)

with open('match_id2.json') as f:
    match_id_lista = json.load(f)

img = Image.open('wzor_zaproszenia.jpg')
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
        home_score1 = match['homeScore'].get('period1')
        home_score2 = match['homeScore'].get('period2')
        away_score1 = match['awayScore'].get('period1')
        away_score2 = match['awayScore'].get('period2')
        home_score3 = match['homeScore'].get('period3')
        home_score4 = match['homeScore'].get('period4')
        away_score3 = match['awayScore'].get('period3')
        away_score4 = match['awayScore'].get('period4')
        home_score5 = match['homeScore'].get('period5')
        away_score5 = match['awayScore'].get('period5')
        name_1 = name_1.encode('utf-8')
        name_2 = name_2.encode('utf-8')
        tournament = tournament.encode('utf-8')
        #home_score1 = home_score1.encode('utf-8')
        #home_score2 = home_score2.encode('utf-8')
        #away_score1 = away_score1.encode('utf-8')
        #away_score2 = away_score2.encode('utf-8')
        draw = ImageDraw.Draw(img)
        #draw.text((100, 100), f"{gosc['imie']} {gosc['nazwisko']}", fill=(0, 0, 0)) #font=font, fill=(0, 0, 0))
        draw.text((100, 60), tournament, fill=(0, 0, 0)) #font=font, fill=(0, 0, 0))
        draw.text((100, 80), name_1, fill=(0, 0, 0)) #font=font, fill=(0, 0, 0))
        draw.text((100, 100), name_2, fill=(0, 0, 0)) #font=font, fill=(0, 0, 0))
        draw.text((100, 120), str(home_score1), fill=(0, 0, 0)) #font=font, fill=(0, 0, 0))
        draw.text((120, 120), str(away_score1), fill=(0, 0, 0)) #font=font, fill=(0, 0, 0))
        draw.text((100, 140), str(home_score2), fill=(0, 0, 0)) #font=font, fill=(0, 0, 0))
        draw.text((120, 140), str(away_score2), fill=(0, 0, 0)) #font=font, fill=(0, 0, 0))

        # zapisz grafikę z imieniem i nazwiskiem gościa
        # Twórz folder "zaproszenia", jeśli nie istnieje
        if not os.path.exists('zaproszenia'):
            os.makedirs('zaproszenia')

        # Zapisz grafikę z imieniem i nazwiskiem zawodnika
        img.save(f'zaproszenia/zaproszenie_{i}.jpg')

        # Ponownie wczytaj wzór zaproszenia przed kolejnym zastosowaniem
        img = Image.open('wzor_zaproszenia.jpg')
        i += 1
        zawodnicy = {
            'tournament': tournament,
            'name1': name_1,
            'name2': name_2
        }
        print(zawodnicy)
        match_id_lista.append(match_id)


with open('match_id2.json', 'w') as f:
    json.dump(match_id_lista, f)



"""
okej, to u gory juz dziala
teraz tutaj dodaj kod z generator zaproszen by stworzyc graafike z nazwisami meczow finished

najs udalo sie, teraz musisz dodac wynik

a potem trzeba ogarnac tak, by nie powtarzaly sie grafiki tylko tworzyly sie nowe dla nowo zakonczonych meczow
"""


        

