import json

with open('tenis.json') as f:
    jsondata = json.load(f)

with open('match_id2.json') as f:
    match_id_lista = json.load(f)

zawodnicy = {}

for match in jsondata['events']:
    status = match['status']['type']
    match_id = match['customId']
    if status == 'finished' and match_id not in match_id_lista:
        print("jestem")
        tournament = match['tournament']['name']
        name_1 = match['homeTeam']['name']
        name_2 = match['awayTeam']['name']
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
tutaj dodaj kod z generator zaproszen by stworzyc graafike z nazwisami meczow finished

a potem trzeba ogarnac tak, by nie powtarzaly sie grafiki tylko tworzyly sie nowe dla nowo zakonczonych meczow"""


        


"""        
    if status == 'finished':
        tournament = match['tournament']['name']
        name_1 = match['homeTeam']['name']
        name_2 = match['awayTeam']['name']

            # Tworzenie słownika z danymi
        zawodnicy = {
            'tournament': tournament,
            'name1': name_1,
            'name2': name_2
        }

        print(f"{tournament} | {name_1} - {name_2} {status}")
        print("Zakończony")
        
            # Zapis do pliku JSON
        with open('zawodnicy.json', 'w') as f:
            json.dump(zawodnicy, f)

        in_progress_ids.remove(match_id)



with open('lista_in_progress_ids.json', 'w') as f:
    json.dump(in_progress_ids, f)

with open('lista_in_progress.json', 'w') as f:
    json.dump(in_progress, f)

print("Koniec")
"""